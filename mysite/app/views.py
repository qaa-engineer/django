from django.http import HttpResponse
from django.template import loader
from .models import Content


def index(request):
    latest_question_list = Content.objects.order_by('id')[:5]
    template = loader.get_template('app/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    question_detail = Content.objects.get(pk=question_id)
    template = loader.get_template('app/detail.html')
    context = {
        'question_detail': question_detail,
    }
    return HttpResponse(template.render(context, request))


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def get_question(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
