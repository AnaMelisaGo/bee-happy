from django.shortcuts import render, redirect
from django.contrib import messages
from userprofiles.forms import ContactUsForm


def home(request):
    """
    Para visualizar la página principal: INDEX.HTML
    """
    return render(request, 'home/index.html', {'home': 'active'})


def blog_post(request):
    """
    Para visualizar la página de post desde index
    """
    return render(request, 'home/blog-post.html')


def contact_us(request):
    """
    Para visualizar formulario de contacto
    """
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            messages.info(request, 'Su mensaje ha sido enviado correctamente')
            return redirect('contact_us')
    else:
        form = ContactUsForm()

    context = {
        'contact': 'active',
        'form': form,
        'redirect': 'home',
    }
    return render(request, 'home/contact_us.html', context)
