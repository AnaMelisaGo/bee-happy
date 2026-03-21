from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from blog.models import Category, Post
from blog.forms import CategoryForm, PostForm
from .forms import RegisterForm, UpdateProfileForm
from .models import Profile

# from django.contrib.auth.decorators import login_required

def login_user(request):
    """
    Para iniciar sesión en la cuenta del usuario usando la funcionalidad de Django: LOGIN

    RECOM: Definir esta función con otro nombre que no sea igual que LOGIN (puede provocar conflicto con el LOGIN de Django)
    """
    if request.user.is_authenticated:
        messages.error(request, 'Ya has iniciado sesión en tu cuenta!')
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido, {username.upper()}. Has iniciado sesión correctamente! Dizzzfruta!')
                return redirect('home')
            else:
                messages.error(request, 'Ha ocurrido un error! Compruebe su usuario o contraseña.')
                return redirect('login')
        else:
            return render(request, 'profiles/login.html', {'login': 'active',})


def logout_user(request):
    """
    Para cerrar sesión del usuario usando la funcionalidad de Django: LOGOUT
    """
    logout(request)
    messages.warning(request, 'Ha cerrado la sesión. Nos vemos pronto!')
    return redirect('home')


def signup_user(request):
    """
    Para crear un nuevo usuario usando el SignUpForm
    desde forms.py con la ayuda de UserCreationForm
    """
    form = RegisterForm()

    if request.user.is_authenticated:
        messages.error(request, 'Acceso no permitido. Cierra sesión para crear un nuevo usuario.')
        return redirect('home')
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'La cuenta se ha creado correctamente!')
                messages.info(request, 'La cuenta se ha creado correctamente!')
                return redirect('signup')
    
    context = {
        'signup': 'active',
        'form': form,
        'redirect': 'login',
    }
    return render(request, 'profiles/signup.html', context)


def profile_list(request):
    """
    Obtener todos los usuarios del blog excepto el usuario de la cuenta autenticada y
    poder verlos en un listado (cards)
    """
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user).order_by('user__username')
        context = {
            'profiles': profiles,
        }
        return render(request, 'profiles/profile_list.html', context)
    else:
        messages.error(request, 'Debe iniciar session para ver esta pagina!')
        return redirect('home')



def profile(request, pk):
    """
    Para visualizar la cuenta de cada usuario

    args: pk es el id de cada usuario
    """
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, pk=pk)
        current_user = request.user
        categorias = Category.objects.all()
        posts = Post.objects.filter(autor=profile.user)
        
        form1 = CategoryForm()
        form2 = PostForm()
        # form3 = None

        if request.method == 'POST':
            # current_user_profile = request.user.profile
            form1 = CategoryForm(request.POST)
            form2 = PostForm(request.POST, request.FILES)
            action = request.POST.get('action')
            if action == 'unfollow':
                current_user.profile.follows.remove(profile)
                current_user.profile.save()
                return redirect('profile', pk=profile.pk)
            elif action == 'follow':
                current_user.profile.follows.add(profile)
                current_user.profile.save()
                return redirect('profile', pk=profile.pk)
            elif action == 'category':
                if current_user.is_superuser:
                    if form1.is_valid():
                        form1.save()
                        messages.success(request, 'Has añadido una nueva categoría.')
                        return redirect('profile', pk=profile.pk)
                    else:
                        form1 = CategoryForm()
            elif action == 'post':
                if form2.is_valid():
                    post = form2.save(commit=False)
                    post.autor = current_user
                    post.save()
                    messages.success(request, 'Szzzzuper! Se ha guardado el post correctamente!')
                    return redirect('profile', pk=profile.pk)
                else:
                    form2 = PostForm()
                    messages.error(request, 'Se ha producido un error.')
    else:
        messages.error(request, 'ACCESO DENEGADO! Debe iniciar sesión para acceder a esta página.')
        return redirect('home')
            
    context = {
        'profile': profile,
        'categorias': categorias,
        'posts': posts,
        'form1': form1,
        'form2': form2,
        # 'form3': form3,
    }
    return render(request, 'profiles/profile.html', context)


def update_profile(request, pk):
    """
    Para modificar datos en la cuenta de usuario

    args: pk es el id de cada usuario
    """
    if request.user.is_authenticated:
        current_user = get_object_or_404(User, pk=pk)
        form = UpdateProfileForm(request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Éxito! Tu cuenta ha sido modificado correctamente.')
            return redirect('profile', pk=current_user.pk)
    else:
        messages.error(request, 'ACCESO DENEGADO!Debe iniciar sesión para acceder a la página.')
        return redirect('home')
    
    context = {
        'form': form,
    }
    return render(request, 'profiles/edit_profile.html', context)