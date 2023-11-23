from django.urls import path
from . import views

urlpatterns = [
    path('capture/', views.capture_image, name='capture_image'),
    path('success/', views.success_page, name='success_page'),
    # Add more URL patterns for different functionalities
]
