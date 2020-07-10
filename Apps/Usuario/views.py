from django.shortcuts import render, HttpResponse, redirect
from .forms import loginForm, registerForm
from ..Preguntas import views as views_questions
from django.contrib.auth import login, logout, authenticate
from .models import User
from django.contrib import messages

# Create your views here.
def home(request):
    if request.user.is_authenticated :
        return redirect('questions')
    else:
        return redirect('login')

def Login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(views_questions.renderQuestions)
            else:
                messages.error(request, "Esta cuenta no existe")
                return render(request, 'login.html', {'form':form})
        else:
            return HttpResponse("Chale")
    else:
        form = loginForm()
        return render(request, 'login.html', {'form':form})

def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            usermame = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            nombres = form.cleaned_data['first_name']
            apellidos = form.cleaned_data['last_name']
            foto = form.cleaned_data.get('foto')

            user = User.objects.filter(username=usermame)
            emailUser = User.objects.filter(email=email)

            if len(user)>0:
                print("Usuario repetido")
                messages.error(request, "Este nombre de usuario ya esta registrado")
                return render(request, 'register.html', {'form' : form})
            
            if len(emailUser)>0:
                print("Email repetido")
                messages.error(request, "Este correo ya se encuentra registrado")
                return render(request, 'register.html', {'form': form})

            user = User(
                username = usermame,
                email = email, 
                first_name = nombres,
                last_name = apellidos,
                foto = foto,
            )

            user.set_password(password)
            user.save()
            messages.success(request, "Usuario creado exitosamente")
            return render(request, 'register.html', {'form': form})
        else:
            messages.error(request, "Formulario no valido, reviselo porfavor")
            return render(request, 'register.html', {'form': form})
    else:
        form = registerForm()
        return render(request, 'register.html', {'form': form})

def Logout(request):
    logout(request)
    return redirect(Login)