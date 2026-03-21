from django.urls import path
from . import views

urlpatterns = [
    path('posts/categoria/<slug:slug>/', views.filtrar_categoria, name='post_categoria'),
    path('posts/todos/', views.post_todos, name='post_todos'),
    path('posts/<int:pk>/<slug:slug>', views.post_leer, name='post_leer'),
    path('posts/editar/<int:pk>/<slug:slug>', views.post_editar, name='post_editar'),
    path('posts/eliminar/<int:pk>/', views.post_eliminar, name='post_eliminar'),
]