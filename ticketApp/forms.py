from django import forms
from .models import Ticket

# Used for the creation of a ticket
class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('ticket_owner', 'project', 'title', 'assignee', 'status', 'description')
        widgets = {
            'ticket_owner': forms.Select(attrs={'class': 'form-control'}),
            'project': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'assignee': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
    }
    
# Update the ticket
class EditTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ( 'project', 'title', 'assignee', 'status', 'description')
        widgets = {
            'project': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'assignee': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'created_at': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'created at ', 'type':'date'}),
            'updated_at': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'updated at ', 'type':'date'}),       
        }