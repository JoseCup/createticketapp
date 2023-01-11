
from django.urls import path, include
# from . import views
# from .views import class based views
from .views import HomeView, CompanyDetailView, AddCompanyView, UpdateCompanyView, DeleteCompanyView
from .views import ProjectDetailView, AddProjectView, UpdateProjectView, DeleteProjectView
from . import views

urlpatterns = [
    # path('', views.home, name='home.html'),
    path('', HomeView.as_view(), name='home'),
    path('features/', views.features, name='feature'),
    path('about/', views.about, name='about'),
    path('pricing/', views.pricing, name='pricing'),
    path('faq/', views.faq, name='faq'),
    path('<int:pk>', CompanyDetailView.as_view(), name='company_detail'),
    path('add_company/', AddCompanyView.as_view(), name='add_company'),
    path('company/edit/<int:pk>', UpdateCompanyView.as_view(), name='update_company'),
    path('company/<int:pk>/remove', DeleteCompanyView.as_view(), name='delete_company'),
    
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project_detail'),
    path('add_project/', AddProjectView.as_view(), name='add_project'),
    path('project/edit/<int:pk>', UpdateProjectView.as_view(), name='update_project'),
    path('project/<int:pk>/remove', DeleteProjectView.as_view(), name='delete_project'),

]