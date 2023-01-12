from django import forms
# from .models import Company, Project
from .models import Ticket
from django.conf import settings
User = settings.AUTH_USER_MODEL
from django.contrib.auth.mixins import LoginRequiredMixin


# Used for the creation of a ticket
class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('ticket_owner', 'title', 'assignee', 'status', 'description')
        widgets = {
            'ticket_owner': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'assignee': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
    }
    
# Update the ticket
class EditTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ( 'title', 'assignee', 'status', 'description')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'assignee': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'created_at': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'created at ', 'type':'date'}),
            'updated_at': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'updated at ', 'type':'date'}),       
        }