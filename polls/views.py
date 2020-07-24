from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse

from .models import Choice, Question


# main index pagee for / url
def main_index(request):
    return render(request, 'index.html')

# get questions and display choices


def index(request):
    latest_questions_list = Question.objects.order_by('-pub_date')

    context = {
        'latest_questions_list': latest_questions_list
    }
    return render(request, 'polls/index.html', context)


# get question details and choices
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question Does not Exist!")
    return render(request, 'polls/detail.html', {'question': question})


# get result
def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
# vote here


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'You didnt select a choice',
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # Always reetun and HttpResponseRedirect after succesfully dealing with post data
        # it will prevent from being posted twice in case hitting backbutton
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
