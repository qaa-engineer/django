from django.urls import path
from django.conf.urls import url
from . import views
from django.views.generic.base import TemplateView
from django.views.generic import RedirectView

app_name = 'app'
urlpatterns = [
    # ex: /
    path('', views.IndexView.as_view(), name='index'),
    # ex: /5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /contacts.html/
    path('contacts.html', views.contacts, name='contacts'),
    # ex: /about.html/
    path('about.html', views.about, name='about'),
    # /all/
    path('all/', views.AllView.as_view()),
    # ex: /results/<>
    path('search/', views.SearchView.as_view(), name='search_results'),
    # Эта строка требуется для отображения robots.txt по адресу .../robots.txt
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    # favicon.ico
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico'), name='favicon'),
]
