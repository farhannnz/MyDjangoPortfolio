from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_page, name='about'),
    path('projects/', views.projects_page, name='projects'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('blog/', views.blog_list, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('certifications/', views.certifications_page, name='certifications'),
    path('contact/', views.contact_page, name='contact'),
]
