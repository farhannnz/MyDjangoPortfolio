from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('education/', views.education, name='education'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('contact/', views.contact, name='contact'),
]
