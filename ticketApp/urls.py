from django.urls import path, include
# Class based views
from .views import TicketView, TicketDetailView, TicketCreateView, TicketUpdateView, TicketDeleteView

urlpatterns = [
    path('', TicketView.as_view(), name='tickets'),
    path('<int:pk>/details/', TicketDetailView.as_view(), name='ticket_details'),
    path('create_ticket/', TicketCreateView.as_view(), name='create_ticket'),
    path('edit/<int:pk>', TicketUpdateView.as_view(), name='update_ticket'),
    path('remove/<int:pk>', TicketDeleteView.as_view(), name='delete_ticket'),

    # add root for a ListView of ticket. The <int:pk> will change to the DetailView.
    # path('<int:pk>', TicketView.as_view(), name='ticket'),
]