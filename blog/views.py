from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Category, Post
from .forms import PostForm, CommentForm


def filtrar_categoria(request, slug):
    """
    Filtrar los posts según categoría

    Args:
        slug: el slug de la categoria
    """
    categoria = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(categoria=categoria, status='publicado')
    current_slug = slug
    context = {
        'categoria_seleccionada': categoria,
        'posts': posts,
        'current_slug': current_slug
    }
    return render(request, 'blog/post_todos.html', context)


def post_todos(request):
    """
    Visualizar todos los post publicados
    """
    posts = Post.objects.filter(status='publicado')
    context = {
        'posts': posts,
        'todos': 'aside-active',
    }
    return render(request, 'blog/post_todos.html', context)


def post_leer(request, pk, slug):
    """
    Para visualizar contenido del cada post

    Args:
        request (pk): Es el id del post
        request (slug): Es el slug del post (creado automaticamente)
    """
    post = get_object_or_404(Post, pk=pk, slug=slug)
    comments = post.comments.filter(post_id=pk).order_by('date_created')
    form = CommentForm()
    liked = False
    if request.user.is_authenticated:
        current_user = request.user
        action = request.POST.get('action')

        if post.likes.filter(id=current_user.id).exists():
            liked = True
        
        if request.method == 'POST':
            if action == 'unfollow':
                current_user.profile.follows.remove(post.autor.profile)
                current_user.profile.save()
                return HttpResponseRedirect(reverse('post_leer', args=[pk, slug]))
            elif action == 'follow':
                current_user.profile.follows.add(post.autor.profile)
                current_user.profile.save()
                return HttpResponseRedirect(reverse('post_leer', args=[pk, slug]))
            elif action == 'comment':
                if request.method == 'POST':
                    form = CommentForm(request.POST)
                    if form.is_valid():
                        comment = form.save(commit=False)
                        comment.name = current_user
                        comment.post = post
                        comment.save()
                        messages.success(request, 'Has comentado a este post.')
                        return HttpResponseRedirect(reverse('post_leer', args=[pk, slug]))

    context = {
        'post': post,
        'user_liked': liked,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog/post_details.html', context)


def like_post(request, pk, slug):
    """
    Función de like y dislike de cada post

    Args:
        request: usuario
        pk: el id del post (primary key)
    """
    post = get_object_or_404(Post, pk=pk, slug=slug)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        return redirect('post_leer', pk=pk, slug=slug)
    else:
        post.likes.add(request.user)
        return redirect('post_leer', pk=pk, slug=slug)


def post_editar(request, pk, slug):
    """
    Para editar el post seleccionado

    Args:
        request: datos del post y el formulario
        pk (int): el id del post seleccionado
        slug: slug del post
    """
    if request.user.is_authenticated:
        current_user = request.user.id
        post = get_object_or_404(Post, pk=pk, slug=slug)
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                messages.success(request, 'Ha editado correctamente')
                return redirect('profile', current_user)
        else:
            form = PostForm(instance=post)
    else:
        messages.error(request, 'Acceso restringido! No tiene permiso para realizar esta acción.')
        return redirect('home')
    
    context = {
        'form': form,
    }

    return render(request, 'blog/post_edit.html', context)


def post_eliminar(request, pk):
    """
    Eliminar el post seleccionado

    Args:
        request: el usuario actual y el boton de eliminar
        pk (int): es el id del post seleccionado
    """
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        current_user = request.user.id
        post.delete()
        messages.success(request, 'El post se ha borrado correctamente!')
        return redirect('profile', current_user)
    else:
        messages.error(request, 'Acceso restringido! No tiene permiso para realizar esta acción.')
