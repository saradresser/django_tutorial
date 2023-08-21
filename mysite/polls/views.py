from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    
    template = "polls/index.html"
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, template, context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    template = "polls/detail.html"
    context = {
        "question": question
    }
    return render(request, template, context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
