from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('delete-todo/<id>/', delete_todo, name='delete_todo'),
    path('update-todo', update_todo, name='update_todo')

]