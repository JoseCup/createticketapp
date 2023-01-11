from django.shortcuts import render
from .models import Ticket
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import TicketForm, EditTicketForm
from django.urls import reverse_lazy
# Create your views here.
# Views are the functions that are called when somebody navigates to an URL.
# They will render a piece of HTML with some particular view.


class TicketView(ListView):
    model = Ticket
    template_name = 'tickets.html'
    ordering = ['updated_at'] # most recent clients first

class TicketDetailView(DetailView):
    model = Ticket
    template_name = 'ticket_details.html'

class TicketCreateView(CreateView):
    model = Ticket
    # Using class-based model form
    form_class = TicketForm
    template_name = 'create_ticket.html'
    def get_initial(self):
        return {'ticket_owner': self.request.user}

class TicketUpdateView(UpdateView):
    model = Ticket
    # Using class-based model form
    form_class = EditTicketForm
    template_name = 'update_ticket.html'
    # Go to tickets after update/edit
    success_url = reverse_lazy('tickets')
    

class TicketDeleteView(DeleteView):
    model = Ticket
    template_name = 'delete_ticket.html'
    # Go to tickets after delete
    success_url = reverse_lazy('tickets')

