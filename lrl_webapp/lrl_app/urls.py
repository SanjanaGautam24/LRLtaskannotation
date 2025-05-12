from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('question/<int:number>/', views.question, name='question'),
    path("success/", views.success, name="success")
]
