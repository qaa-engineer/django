from django.db.models import Q
from django.http import HttpResponse
from django.http import Http404
from .models import Content
from django.shortcuts import render
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Content.objects.order_by('id')[:7]


def detail(request, question_id):
    try:
        question_detail = Content.objects.get(pk=question_id)
    except Content.DoesNotExist:
        raise Http404("Question does not exist")
    context = {
        'question_detail': question_detail,
    }
    return render(request, 'detail.html', content_type='text/html', context=context)


def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

class AllView(generic.ListView):
    template_name = 'all.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Content.objects.order_by('id').all()


class SearchView(generic.ListView):
    model = Content
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Content.objects.filter(
            Q(title__icontains=query)
        )
        return object_list
