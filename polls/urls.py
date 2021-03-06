#responsible for the URL paths

from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/wrong/', views.wrong, name='wrong'),
    # ex: /polls/5/
    path('<int:pk>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]