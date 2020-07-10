from django import forms
from django.forms import ModelForm
from .models import User

class loginForm(forms.Form):
    username=forms.CharField(
        max_length=50,
        min_length=4,
        required=True,
        label="Ingresa tu nombre de usuario",
        widget=forms.TextInput(attrs={
            'placeholder' : 'user',
            'class' : 'form-control',
        })
    )

    password=forms.CharField(
        max_length=50,
        min_length=6,
        required=True,
        label="Ingresa tu contraseña",
        widget=forms.PasswordInput(attrs={
            'placeholder' : 'password',
            'class' : 'form-control',
        })
    )

class registerForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email','first_name','last_name','foto']
        widgets = {
            'username' : forms.TextInput(attrs={
                'class':'form-control',
                'placeholder' : 'Username'
                }),
            'password' : forms.PasswordInput(attrs={
                'class':'form-control',
                'placeholder':'********'
                }),
            'email' : forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder' : 'example@something.com'
                }),
            'first_name' : forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Name'
                }),
            'last_name' : forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Last name'
            }),
            'foto' : forms.ClearableFileInput(attrs={
                'class' : 'form-control',
            }),
        }
        help_texts={
            'username':'El nombre debe tener almenos 4 caracteres',
            'password':'La contraseña debe contener almenos 6 caracteres',
        }
        labels={
            'foto': 'Foto',
        }