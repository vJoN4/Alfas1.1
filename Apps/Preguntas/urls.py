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
    path('profile', views_questions.renderProfile, name='profile'),
    path('myquestions', views_questions.renderUserQuestions, name='myquestions'),
    path('editquestionsurl', views_questions.editQuestions, name='editquestionsurl'),
    path('deletequestion', views_questions.deleteQuestion, name='deletequestionurl'),
    path('editanswer',views_questions.editAnswer, name='editanswerurl'),
    path('deleteanswer',views_questions.deleteAnswer, name='deleteanswerurl'),
    path('editprofile', views_questions.editProfile, name='editprofileurl'),
    path('bycategory/<str:categoria>', views_questions.renderQuestionsByCategory, name='bycategory'),
]