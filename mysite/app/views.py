from django.http import HttpResponse
from django.http import Http404
from .models import Content
from django.shortcuts import render
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Content.objects.order_by('id')[:10]


def detail(request, question_id):
    try:
        question_detail = Content.objects.get(pk=question_id)
    except Content.DoesNotExist:
        raise Http404("Question does not exist")
    title = question_detail.title
    post = question_detail.post
    context = {
        'question_detail': question_detail,
        'title': title,
        'post': post,
    }
    # FixME
    return render(request, 'detail.html', content_type='text/html', context=context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def get_question(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
