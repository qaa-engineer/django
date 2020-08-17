from django.urls import path

from . import views
from django.views.generic.base import TemplateView

app_name = 'app'
urlpatterns = [
    # ex: /
    path('', views.IndexView.as_view(), name='index'),
    # ex: /5/
    path('<int:question_id>/', views.detail, name='detail'),
    # /all/
    path('all/', views.AllView.as_view()),
    # ex: /results/<>
    path('search/', views.SearchView.as_view(), name='search_results'),
    # Эта строка требуется для отображения robots.txt по адресу .../robots.txt
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
]
