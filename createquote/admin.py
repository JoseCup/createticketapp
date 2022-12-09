from django.contrib import admin
from .models import Company, Project
# Import Ticket model from ticketApp app from the app registry in createquoteproj settings.py
from ticketApp.models import Ticket

class TicketAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_filter = ('status', 'assignee')
    list_display = ('id', 'title', 'status', 'assignee', 'description', 'updated_at')
    search_fields = ['title','status']


# @admin.register(Service)
# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ['name', 'qty', 'active']
#     list_filter = ['active']
#     search_fields = ['name']
#     list_per_page = 50
#     fields = ['active', 'name', 'qty', 'price', 'discount_price']

admin.site.register(Company)
admin.site.register(Project)
# admin.site.register(Order)
# admin.site.register(OrderItem)
admin.site.register(Ticket, TicketAdmin)
 