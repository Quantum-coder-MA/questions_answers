from django.http.response import HttpResponse, JsonResponse   
from django.shortcuts import render
import random
from .models import *
# Create your views here.
from django.http import HttpResponse
def home(request):
    return render(request, 'nigga.html ')
#{    
#    'status' : True
#    'data' : [
#           {},  
#         ]
#}







def get_questions_answers(request):
    try:
        question_objs = list(Question.objects.all())
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