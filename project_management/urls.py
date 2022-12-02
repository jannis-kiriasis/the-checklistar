from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.ProjectList, name='dashboard'),
    path('create-project', views.CreateProject, name='create-project'),
    path('<slug:slug>/', views.ProjectDetails.as_view(), name='project-details'),
    path('edit/<project_id>', views.EditProject, name='edit'),
    path('approve/<projectApproval_id>', views.ApproveProject, name='approve'),
    path('delete/<project_id>', views.DeleteProject, name='delete'),
    path('complete/<project_id>', views.CompleteProject, name='complete'),
    path('my-projects', views.MyProjectList, name='my-projects'),
    path('my-approvals', views.MyApprovalsList, name='my-approvals'),
]
