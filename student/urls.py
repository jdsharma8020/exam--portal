from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.index, name='index'),
    path('exams', views.exams, name='exams'),
    path('results', views.results, name='results'),
]