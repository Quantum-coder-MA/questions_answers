from django.urls import path
from . import views

urlpatterns = [
    
    
    path('', views.home, name='home'),
    
    
    
    
    path('api/get-questions-answers/', views.get_questions_answers, name='get_questions_answers'),
    path('questions_answers/', views.questions_answers , name="questions_answers")
]