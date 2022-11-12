from django.shortcuts import render
# importing generics - list displays list of objects, detail shows one object's details
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from models.py
from .models import Client, Project
from .forms import ClientForm, EditClientForm, ProjectForm, EditProjectForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Client
    template_name = 'home.html'
    # ordering = ['-client_date'] # most recent clients first
    # ordering = ['-id']

class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_details.html'

class AddClientView(CreateView):
    model = Client
    # form_class for adding clients
    form_class = ClientForm
    template_name = 'add_client.html'
    # fields = '__all__' 
    # ClientForm takes care of fields

class UpdateClientView(UpdateView):
    model = Client
    form_class = EditClientForm
    template_name = 'update_client.html'
    # fields = [ 'email', 'phone', 'location','company' ]

class DeleteClientView(DeleteView):
    # we need a success_url to tell us where to go after deleting a client
    # use reverse_lazy for the success_url
    model = Client
    template_name = 'delete_client.html'
    success_url = reverse_lazy('home')

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_details.html'

class AddProjectView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'add_project.html'

class UpdateProjectView(UpdateView):
    model = Project
    form_class = EditProjectForm
    template_name = 'update_project.html'

class DeleteProjectView(DeleteView):
    model = Project
    template_name = 'delete_project.html'
    success_url = reverse_lazy('home')