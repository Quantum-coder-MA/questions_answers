from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import random
from django.urls import reverse
from .models import *
# Create your views here.
from django.http import HttpResponse
def home(request):
    context = {'categories': Category.objects.all()}
    
    if request.GET.get('category'):
        category = request.GET.get('category')
        url = reverse('questions_answers') + f'?category={category}'
        return redirect(url)
    
    return render(request, 'home.html', context)




def questions_answers(request):
    return render(request, 'home.html')



def get_questions_answers(request):
    try:
        question_objs = list(Question.objects.all())
        
        if request.GET.get('category'):
            question_objs = question_objs.filter(category_category_name_icontains=request.GET.get('category'))
        question_objs = list(question_objs)
        
        
        
        data = []
        random.shuffle((question_objs))
        
        
        print(question_objs)
        
        for question_objs in question_objs:
            
            data.append({
                "category" : question_objs.category.category_name,
                "question_text": question_objs.question_text,
                "marks" : question_objs.marks,
                "answer": question_objs.get_Answer()
            })
        playload = {'status' : True, 'data': data}
        
        return JsonResponse(playload)
        
    except Exception as e:
        print(e)
        return HttpResponse("Somthing went wrong")