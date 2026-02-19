from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects_view, name='projects'),
    path('research/', views.research, name='research'),
    path('publications/', views.publications, name='publications'),
    path('resources/', views.resources, name='resources'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
]