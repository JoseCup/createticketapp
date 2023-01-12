from django.urls import path
from .views import index

urlpatterns = [
    # path('', views.home, name='home.html'),
    path('', index),
  

]