"""Define URL schemas for knowledge_logs."""

from django.urls import path

from . import views

app_name = 'knowledge_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]
