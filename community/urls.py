from django.urls import path
from .views import *

app_name = 'community'

urlpatterns = [
    path('', forum, name='forum'),
    path('<int:question_id>', detail, name='detail'),
    path('answer/create/<int:question_id>',  answer_create, name='answer_create'),
    path('question/create/', question_create, name='question_create'),
    path('modify/<int:question_id>/', question_modify, name='question_modify'),
]
