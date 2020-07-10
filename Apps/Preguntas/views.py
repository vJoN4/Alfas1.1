from django.shortcuts import render, HttpResponse
from .models import pregunta, respuesta
from ..Usuario.models import User
from datetime import date
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def renderHome(request):
    return render(request, 'homeBase.html')

@login_required
def renderQuestions(request):
    allQuestions = pregunta.objects.all().order_by('-fecha')
    categoria = "Todas las categorias"
    return render(request, 'questions.html', {
        'questions': allQuestions,
        'categoria': categoria,
    })

@login_required
def renderAnswers(request, idPregunta):
    question = pregunta.objects.get(id=idPregunta)
    answers = respuesta.objects.filter(pregunta__id=idPregunta)
    return render(request, 'answers.html', {
        'question':question,
        'answers' : answers,
    })

@login_required
def uploadQuestionTemplate(request):
    allQuestions = pregunta.objects.all().order_by('-fecha')
    # print(request.user.id)
    return render(request, 'uploadQuestion.html', {'questions': allQuestions})

@login_required
def uploadQuestion(request):
    try:
        contenido = request.POST['contenido']
        descripcion = request.POST['descripcion']
        categoria = request.POST['categoria']

        pregunta.objects.create(
            contenido = contenido,
            descripcion = descripcion,
            fecha = date.today(),
            categoria = categoria,
            usuario = request.user,
        )
        return HttpResponse(True)
    except Exception as identifier:
        return HttpResponse(False)

@login_required
def uploadAnswersTemplate(request, idPregunta):
    question = pregunta.objects.get(id=idPregunta)
    answers = respuesta.objects.filter(pregunta__id=idPregunta)
    return render(request, 'uploadAnswers.html', {
        'question' : question,
        'answers' : answers,
    })

@login_required
def uploadAnswers(request):
    try:
        contenido = request.POST['contenido']
        idQuestion = request.POST['idQuestion']

        # print(contenido)
        # print(idQuestion)

        respuesta.objects.create(
            contenido = contenido,
            fecha = date.today(),
            usuario = request.user,
            pregunta = pregunta.objects.get(id=idQuestion),
        )
        return HttpResponse(True)
    except Exception as identifier:
        return HttpResponse(False)

@login_required
def renderProfile(request):
    return render(request, 'profile.html')

@login_required
def renderUserQuestions(request):
    userQuestions = pregunta.objects.filter(usuario=request.user).order_by('-fecha')
    return render(request, 'userQuestions.html', {'questions': userQuestions})

@login_required
def editQuestions(request):
    contenido = request.POST['contenido']
    descripcion = request.POST['descripcion']
    categoria = request.POST['categoria']
    idQuestion = request.POST['idQuestion']

    question = pregunta.objects.get(id=idQuestion)
    try:    
        question.contenido = contenido
        question.descripcion = descripcion
        question.categoria = categoria
        question.fecha = date.today()
        question.save()
        return HttpResponse(True)
    except Exception as identifier:
        return False

@login_required
def deleteQuestion(request):
    try:
        idQuestion = request.POST['idQuestion']
        question = pregunta.objects.get(id=idQuestion)
        question.delete()
        return HttpResponse(True)
    except Exception as identifier:
        return HttpResponse(False)

@login_required
def editAnswer(request):
    try:
        contenido = request.POST['contenido']
        idAnswer = request.POST['idAnswer']

        answer = respuesta.objects.get(id=idAnswer)

        answer.contenido = contenido
        answer.fecha = date.today()
        answer.save()
        return HttpResponse(True)
    except Exception as identifier:
        return HttpResponse(False)

@login_required
def deleteAnswer(request):
    try:
        idAnswer = request.POST['idAnswer']
        answer = respuesta.objects.get(id=idAnswer)
        answer.delete()
        return HttpResponse(True)
    except Exception as identifier:
        return HttpResponse(False)

@login_required
def editProfile(request):
    username = request.POST['username']
    nombres = request.POST['nombres']
    apellidos = request.POST["apellidos"]
    correo = request.POST['correo']
    try:
        foto = request.FILES["foto"]
    except Exception as error:
        user = User.objects.get(id=request.user.id)
        user.username = username
        user.first_name = nombres
        user.last_name = apellidos
        user.email = correo
        user.save()
    else:
        user = User.objects.get(id=request.user.id)
        user.username = username
        user.first_name = nombres
        user.last_name = apellidos
        user.email = correo
        user.foto = foto
        user.save()
    return HttpResponse(True)

@login_required
def renderQuestionsByCategory(request, categoria):
    questionsByCategory = pregunta.objects.filter(categoria=categoria).order_by('-fecha')
    return render(request, 'questions.html', {
        'questions': questionsByCategory,
        'categoria': categoria,
    })