from . import views
from django.urls import path


urlpatterns = [
    path('', views.ProjectList.as_view(), name='dashboard'),
    path('create-project', views.CreateProject, name='create-project'),
]
