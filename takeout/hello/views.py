from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import loader

from .models import Question, Choice

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #pdb.set_trace()
    #output = ', '.join([q.question_text for q in latest_question_list])
    template = loader.get_template('hello/index.html')
    context = {'latest_question_list': latest_question_list,}
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    error_message = None
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'hello/detail.html', {'question': question, 'error_message': error_message})        


def results(request, question_id):
    response = "You are looking  results of %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'hello/detail.html', \
            {'question': question, 'error_message': "you didn't select any choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('hello:results', args=(question.id,)) )







