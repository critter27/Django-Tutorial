from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader
from django.shortcuts import render

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #output = ', '.join([q.question_text for q in latest_question_list])   
    context = {'latest_question_list': latest_question_list}
    #return HttpResponse(template.render(context,'polls/index.html',request))
    #return HttpResponse("Hello World. You're at the polls index bih.")
    return render(request,'polls/index.html',context)
    
def detail(request, question_id):
    try:
        Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return HttpResponse("You're looking at question %s: " % question_id)
    
def results(request, question_id):
    return HttpResponse("You're looking at the results for question %s: " % question_id)
    
def vote(request, question_id):
    return HttpResponse("You're voting on question %s: " % question_id)
# Create your views here.
