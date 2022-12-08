from django.db import models
from django.urls import reverse
from datetime import datetime, date
# Need to bind a ticket to a user - multiple people can handle a ticket.
from django.contrib.auth.models import User


# Create your models here.
# Models describe the logic of the app

class TicketStatus(models.TextChoices):
    TO_DO = 'To Do'
    IN_PROGRESS = 'In Progress'
    IN_REVIEW = 'In Review'
    DONE = 'Done'

class Ticket(models.Model):
    title = models.CharField(max_length=100)
    assignee = models.ForeignKey(User, null=True, blank = True, on_delete=models.CASCADE)
    status = models.CharField(max_length=25, choices=TicketStatus.choices, default=TicketStatus.TO_DO)
    description = models.CharField(max_length=255,blank=True, null=True)
    # description = models.TextField()
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True)

    class Meta:
            ordering = ['title']
            permissions = [
                ("change_ticket_status", "Can change the status of a ticket"),
                ("close_ticket", "Can close a ticket by changing its status as Done"),
            ]
        
    def __str__(self):
            return self.title

    def get_absolute_url(self):
        # return reverse("client_detail", args=(str(self.id)))
        return reverse("home") # or just go back home


