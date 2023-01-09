from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name="projects"),
    path('post/<str:pk>/', views.project, name="project"),

    path('create-post/', views.createProject, name="create-project"),

    path('update-post/<str:pk>/', views.updateProject, name="update-project"),

    path('delete-post/<str:pk>/', views.deleteProject, name="delete-project"),

]
