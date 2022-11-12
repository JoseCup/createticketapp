# Members urls
# Don't forget the comma in urlpatterns
from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView
# user views that come with authentication system from views
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    # instead of auth view for success_url redirect, create PasswordsChangeView() in views
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('password_success', views.password_success, name="password_success"),
]
