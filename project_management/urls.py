from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.project_list, name='dashboard'),
    path('create-project', views.create_project, name='create-project'),
    path(
        'project-details/<slug:slug>/',
        views.project_details,
        name='project-details'),
    path('edit/<project_id>', views.edit_project, name='edit'),
    path(
        'approve/<projectApproval_id>',
        views.approve_project,
        name='approve'
        ),
    path('delete/<project_id>', views.delete_project, name='delete'),
    path('complete/<project_id>', views.complete_project, name='complete'),
    path('my-projects', views.my_project_list, name='my-projects'),
    path('my-approvals', views.my_approvals_list, name='my-approvals'),
    path('notifications', include('notification.urls')),
]

# add a flag for
# handling the 404 error
handler404 = 'project_management.views.error_404_view'

# add a flag for
# handling the 500 error
handler500 = 'project_management.views.error_500_view'
