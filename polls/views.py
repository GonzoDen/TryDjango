#responsible for the pages and their view

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import loader
from django.views import generic

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_name'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            'question': question,
            'error_message': "U didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id, )))



"""def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list' : latest_question_list
    }
    #return HttpResponse(output)
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def wrong(request, question_id):
    response = "Wrong at q %s"
    return HttpResponse(response % question_id)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
"""
