from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Synchronizes data between users and posts through 'urlpatterns'
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', views.getRoutes),
    path('posts/', views.getProjects),
    path('posts/<str:pk>/', views.getProject),
    path('posts/<str:pk>/vote/', views.projectVote),

    path('remove-tag/', views.removeTag)
]
