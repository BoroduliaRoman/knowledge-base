"""Define URL schemas for users"""

from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # Include URL auth by default
    path('', include('django.contrib.auth.urls')),
]