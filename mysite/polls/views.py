from django.shortcuts import render
from django.http import HttpResponse, Http404


from .models import Question


def index(request):
    """ Creates an HTTP response for the index route. """

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list, }
                    # request, template, optional payload (dictionary)
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    """ Takes in a question_id and creates an HTTP response
    for the question detail route. """

    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist.")
    return render(request, 'polls/detail.html', {'question': question})


def results(results, question_id):
    """ Takes in a question_id and creates an HTTP response with
    information about a particular question's results. """

    response = "You're looking at the results of question {}.".format(question_id)

    return HttpResponse(response)


def vote(request, question_id):
    """ HttpResponse returns a voting form for a particular question. """

    return HttpResponse("You're voting on question {}".format(question_id))
