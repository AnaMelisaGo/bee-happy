from .models import Category

def category_list(request):
    return {
        'categorias': Category.objects.all(),
    }