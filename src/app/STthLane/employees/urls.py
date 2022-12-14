from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('edit/list/', views.showUsers, name='edit'),
    path('del/<user_id>', views.removeEmployee, name='remove-employee'),
    path('edit/<user_id>', views.editEmployee, name='edit-employee')
]
