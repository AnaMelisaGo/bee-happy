from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
# from ckeditor.widgets import CKEditorWidget

class BootstrapForm:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            widget = field.widget

            if isinstance(widget, forms.CheckboxInput):
                css_class = "form-check-input"
            else:
                css_class = "form-control"

            if self.errors.get(field_name):
                css_class += " is-invalid"
                
            widget.attrs.update({
                'class': css_class,
                'placeholder': field.label,
            })

            # if isinstance(widget, CKEditorWidget):
            #     field.label = ""

class RegisterForm(BootstrapForm, UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ContactUsForm(BootstrapForm, forms.Form):
    ASUNTO_CHOICES = [
        ('', '-- Seleccione una opcion --'),
        ('informacion', 'Información'),
        ('rescatar', 'Rescatar abejas'),
        ('incidencias', 'Incidencias'),
        ('sugerencias', 'Sugerencias'),
    ]

    nombre = forms.CharField(max_length=100, required=True, label='Nombre')
    email = forms.EmailField(required=True, label='Email')
    asunto = forms.ChoiceField(choices=ASUNTO_CHOICES, label='Asunto')
    mensaje = forms.CharField(required=True, max_length=1000, widget=forms.Textarea(attrs={'rows': 10}), label='Mensaje')

class UpdateProfileForm(BootstrapForm, forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class UpdatePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super.__init__(self, *args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})