from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('parking/', include('parking_system.urls')),  # Include app's URLs
]
