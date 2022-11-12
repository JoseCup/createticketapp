
from django.urls import path, include
# from . import views
# from .views import class based views
from .views import HomeView, ClientDetailView, AddClientView, UpdateClientView, DeleteClientView
from .views import ProjectDetailView, AddProjectView, UpdateProjectView, DeleteProjectView

urlpatterns = [
    # path('', views.home, name='home.html'),
    path('', HomeView.as_view(), name='home'),
    path('client/<int:pk>', ClientDetailView.as_view(), name='client_detail'),
    path('add_client/', AddClientView.as_view(), name='add_client'),
    path('client/edit/<int:pk>', UpdateClientView.as_view(), name='update_client'),
    path('client/<int:pk>/remove', DeleteClientView.as_view(), name='delete_client'),
    
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project_detail'),
    path('add_project/', AddProjectView.as_view(), name='add_project'),
    path('project/edit/<int:pk>', UpdateProjectView.as_view(), name='update_project'),
    path('project/<int:pk>/remove', DeleteProjectView.as_view(), name='delete_project'),

]