
from django.urls import path, include
from .views import TicketView, TicketDetailView, TicketCreateView, TicketUpdateView, TicketDeleteView
# from . import views
# from .views import class based views
# from .views import HomeView, CompanyDetailView, AddCompanyView, UpdateCompanyView, DeleteCompanyView
# from .views import ProjectDetailView, AddProjectView, UpdateProjectView, DeleteProjectView
from . import views

urlpatterns = [
    # path('', views.home, name='home.html'),
    path('', TicketView.as_view(), name='home'),
    path('features/', views.features, name='feature'),
    path('about/', views.about, name='about'),
    path('pricing/', views.pricing, name='pricing'),
    path('faq/', views.faq, name='faq'),
    
    path('<int:pk>/details/', TicketDetailView.as_view(), name='ticket_details'),
    path('create_ticket/', TicketCreateView.as_view(), name='create_ticket'),
    path('edit/<int:pk>', TicketUpdateView.as_view(), name='update_ticket'),
    path('remove/<int:pk>', TicketDeleteView.as_view(), name='delete_ticket'),

]