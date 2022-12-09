from django.shortcuts import render
# importing generics - list displays list of objects, detail shows one object's details
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from models.py
from .models import Company, Project
from .forms import CompanyForm, EditCompanyForm, ProjectForm, EditProjectForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Company
    template_name = 'home.html'
    # ordering = ['-Company_date'] # most recent Companys first
    # ordering = ['-id']

class CompanyDetailView(DetailView):
    model = Company
    template_name = 'company_details.html'

class AddCompanyView(CreateView):
    model = Company
    # form_class for adding Companys
    form_class = CompanyForm
    template_name = 'add_company.html'
    # fields = '__all__' 
    # CompanyForm takes care of fields

class UpdateCompanyView(UpdateView):
    model = Company
    form_class = EditCompanyForm
    template_name = 'update_company.html'
    # fields = [ 'email', 'phone', 'location','company' ]

class DeleteCompanyView(DeleteView):
    # we need a success_url to tell us where to go after deleting a Company
    # use reverse_lazy for the success_url
    model = Company
    template_name = 'delete_company.html'
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