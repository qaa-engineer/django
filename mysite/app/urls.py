from django.urls import path

from . import views

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

]
