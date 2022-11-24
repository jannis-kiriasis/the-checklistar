from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.ProjectList.as_view(), name='dashboard'),
    path('create-project', views.CreateProject, name='create-project'),
    path('<slug:slug>/', views.ProjectDetails.as_view(), name='project-details'),
]
