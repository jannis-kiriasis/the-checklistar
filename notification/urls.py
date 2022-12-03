from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.notifications, name='notifications'),
]
