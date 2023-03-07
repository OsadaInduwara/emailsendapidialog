from django.urls import path

from . import views

urlpatterns = [
    path('mail/', views.send_email, name='send_email'),

]
