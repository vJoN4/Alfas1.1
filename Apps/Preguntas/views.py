from django.shortcuts import render, HttpResponse
from .models import pregunta, respuesta
from datetime import date


# Create your views here.
def renderHome(request):
    return render(request, 'homeBase.html')

def renderQuestions(request):
    allQuestions = pregunta.objects.all().order_by('-fecha')
    return render(request, 'questions.html', {'questions': allQuestions})

def renderAnswers(request, idPregunta):
    question = pregunta.objects.get(id=idPregunta)
    answers = respuesta.objects.filter(pregunta__id=idPregunta)
    return render(request, 'answers.html', {
        'question':question,
        'answers' : answers,
    })

def uploadQuestionTemplate(request):
    allQuestions = pregunta.objects.all().order_by('-fecha')
    # print(request.user.id)
    return render(request, 'uploadQuestion.html', {'questions': allQuestions})

def uploadQuestion(request):
    try:
        contenido = request.POST['contenido']
        descripcion = request.POST['descripcion']
        categoria = request.POST['categoria']

        # print(contenido)
        # print(descripcion)
        # print(categoria)
        # print(request.user.id)
        # print(date.today())
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

def uploadAnswersTemplate(request, idPregunta):
    question = pregunta.objects.get(id=idPregunta)
    answers = respuesta.objects.filter(pregunta__id=idPregunta)
    return render(request, 'uploadAnswers.html', {
        'question' : question,
        'answers' : answers,
    })

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