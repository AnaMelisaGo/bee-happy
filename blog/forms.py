from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Category, Post
from userprofiles.forms import BootstrapForm

class CategoryForm(BootstrapForm, forms.ModelForm):
    name = forms.CharField(max_length=100, required=True, label="Nombre")

    class Meta:
        model = Category
        fields = ['name']


class PostForm(BootstrapForm, forms.ModelForm):
    # categoria = forms.ModelChoiceField(queryset=Category.objects.none())
    
    cuerpo = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = ['titulo', 'categoria', 'resumen', 'cuerpo', 'imagen_principal', 'status']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['categoria'].queryset = Category.objects.all()
