from django import forms
from .models import Company, Project
from django.conf import settings
User = settings.AUTH_USER_MODEL
from django.contrib.auth.mixins import LoginRequiredMixin

class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ( 'company_owner','company_name', 'email', 'location', 'phone')
        widgets = {

            'company_owner': forms.Select(attrs={'class': 'form-control', 'readonly':'readonly'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EditCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ( 'company_name', 'email', 'location', 'phone')
        widgets = {
            # Do not allow edit form to modify user_company
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_owner', 'project_name', 'description', 'website', 'budget', 'start_date', 'end_date')
        widgets = {
            'project_owner': forms.Select(attrs={'class': 'form-control'}),
            'project_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.TextInput(attrs={'class': 'form-control'}),
            'budget': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a start date', 'type':'date'}),
            'end_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select an end date', 'type':'date'}),
        }

class EditProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_name', 'description', 'website', 'budget', 'start_date', 'end_date')
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.TextInput(attrs={'class': 'form-control'}),
            'budget': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a start date', 'type':'date'}),
            'end_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select an end date', 'type':'date'}),
        }