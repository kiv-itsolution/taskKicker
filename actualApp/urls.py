from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('kick_task/', views.kick_task, name='kick_task')
]
