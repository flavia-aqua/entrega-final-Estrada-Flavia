from django import forms
from .models import Blogs
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, User

class CursoFormulario(forms.Form):
    nombreCurso = forms.CharField()
    nivelCurso = forms.CharField()
    fechaCurso = forms.DateField()

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['titulo', 'subtitulo', 'tema', 'cuerpo', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'nombreBlog',
                'placeholder': 'Ingrese el nombre de un blog',
                'required': True
            }),
            'subtitulo': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'subtituloBlog',
                'placeholder': 'Ingrese el subtítulo',
                'required': True
            }),
            'tema': forms.Select(attrs={
                'class': 'form-select',
                'id': 'temaBlog',
                'aria-label': 'Default select example'
            }),
            'cuerpo': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'cuerpoBlog',
                'placeholder': 'Ingrese el contenido del blog',
                'rows': 5
            }),
            'imagen': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'id': 'imagenBlog'
            }),
        }

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa tu nombre de usuario',
            'id': 'id_username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa tu contraseña',
            'id': 'id_password'
        })
    )

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        label="Usuario",
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Ingresa tu nombre de usuario',
            'id': 'id_username'
        })
    )
    email = forms.EmailField(
        required=True,
        label="Correo Electrónico",
        widget=forms.EmailInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Ingresa tu correo electrónico',
            'id': 'id_email'
        })
    )
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Ingresa tu contraseña',
            'id': 'id_password1'
        })
    )
    password2 = forms.CharField(
        label="Repetir Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Repite tu contraseña',
            'id': 'id_password2'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_staff = True  # Establecer is_staff a True
        if commit:
            user.save()
        return user