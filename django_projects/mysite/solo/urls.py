from django.urls import path

from . import views

app_name = 'solo'
urlpatterns = [
    path('', views.SoloList.as_view(), name='index'),
]