from django.urls import path, include
from . import views as views_questions

urlpatterns = [
    path('', views_questions.renderHome, name='home'),
    path('home', views_questions.renderQuestions, name='questions'),
    path('answers/<int:idPregunta>', views_questions.renderAnswers, name='answers'),
    path('addquestion', views_questions.uploadQuestionTemplate, name='upQuestion'),
    path('addquestionurl', views_questions.uploadQuestion, name='upQuestionURL'),
    path('addanswers/<int:idPregunta>', views_questions.uploadAnswersTemplate, name='upAnswer'),
    path('addanswersurl', views_questions.uploadAnswers, name='upAnswerURL'),
]