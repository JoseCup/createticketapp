from django.shortcuts import render
# importing generics - list displays list of objects, detail shows one object's details
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import TicketForm, EditTicketForm
# from .forms import CompanyForm, EditCompanyForm, ProjectForm, EditProjectForm
from django.urls import reverse_lazy
from .models import Ticket

class HomeView(ListView):
    template_name = 'home.html'
    # ordering = ['-Company_date'] # most recent Companys first
    # ordering = ['-id']

def features(request):
    return render(request, 'features.html')

def about(request):
    return render(request, 'about.html')

def pricing(request):
    return render(request, 'pricing.html')

def faq(request):
    return render(request, 'faq.html')



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

