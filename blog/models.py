from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from tinymce.models import HTMLField
# from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        """ Función para generar slug a cada categoría añadido """
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        """ Devuelve el nombre de la categoría """
        return self.name

class Post(models.Model):
    STATUS_CHOICES = [
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado')
    ]

    titulo = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    categoria = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='posts', blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    resumen = models.CharField(max_length=100, null=True, blank=True)
    # cuerpo = RichTextField(null=True, blank=True)
    # cuerpo = models.TextField(null=True, blank=True)
    cuerpo = HTMLField(null=True, blank=True)
    imagen_principal = models.ImageField(upload_to='images/', null=True, blank=True)
    actualizado = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='borrador')
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        """ Ordenar los posts del más reciente a lo más antiguo """
        ordering = ['-fecha_publicacion']
    
    def save(self, *args, **kwargs):
        """ Función para generar slug a cada post creado """
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        """ Devolver el título del post """
        return self.titulo
    
    def number_of_likes(self):
        """ Función para contar el total de likes de cada post """
        return self.likes.count()
    
class Comment(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commented')
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return f'Comment for {self.post} by {self.name}'
