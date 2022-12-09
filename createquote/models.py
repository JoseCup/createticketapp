from django.db import models
from django.urls import reverse
from django.conf import settings
User = settings.AUTH_USER_MODEL

# User has company has projects has ticket?
# User has company has ticket
# change Client to Company
class Company(models.Model):
    
    # Change client_name to user_company
    user_company = models.ForeignKey("Company", on_delete=models.CASCADE, null=True, blank=True)
    company_name = models.CharField(max_length=24, default='A Simple Company')
    email = models.EmailField(max_length = 25)
    location = models.CharField(max_length = 200)
    phone = models.CharField(max_length=15, null=True, blank=False)
    company_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.company_name) 
    
    # target 'client_detail' path from urls.py after creating something in our model
    # args take us to new client_detail page with self.id
    def get_absolute_url(self):
        # return reverse("client_detail", args=(str(self.id)))
        return reverse("home") # or just go back home

class Project(models.Model):
    project_name = models.CharField(max_length = 255)
    project_owner = models.ForeignKey(Company, related_name="projects", on_delete=models.CASCADE)
    description = models.TextField()
    website = models.URLField(max_length=100)
    budget = models.CharField(max_length=12)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.project_name 

    def get_absolute_url(self):
        return reverse("home")

# service