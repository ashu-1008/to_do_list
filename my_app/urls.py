from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    path('', views.home, name='home'),
    path('add_todo/', views.add_todo),
    path('delete_todo/<int:todo_id>/', views.delete_todo),
]
