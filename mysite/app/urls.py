from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    # ex: /
    path('', views.IndexView.as_view(), name='index'),
    # ex: /5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /5/question/
    path('<int:question_id>/question/', views.get_question, name='get_question'),
]