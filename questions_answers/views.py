from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import random
from django.urls import reverse
from .models import Category, Question

def home(request):
    context = {'categories': Category.objects.all()}
    
    if request.GET.get('category'):
        category = request.GET.get('category')
        url = reverse('questions_answers') + f'?category={category}'
        return redirect(url)
    
    return render(request, 'home.html', context)

def questions_answers(request):
    return render(request, 'questions_answers.html')

def get_questions_answers(request):
    try:
        question_objs = Question.objects.all()
        
        if request.GET.get('category'):
            question_objs = question_objs.filter(category__category_name__icontains=request.GET.get('category'))
        
        question_objs = list(question_objs)
        random.shuffle(question_objs)
        
        data = []
        for question in question_objs:
            data.append({
                "category": question.category.category_name,
                "question_text": question.question_text,
                "marks": question.marks,
                "answer": question.get_Answer()
            })
        
        payload = {'status': True, 'data': data}
        return JsonResponse(payload)
    
    except Exception as e:
        print(e)
        return HttpResponse("Something went wrong")
