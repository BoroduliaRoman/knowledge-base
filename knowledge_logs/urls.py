"""Define URL schemas for knowledge_logs."""

from django.urls import path

from . import views

app_name = 'knowledge_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Topics page
    path('topics/', views.topics, name='topics'),
    # Page with detail info by each topic
    path('topics/<int:topic_id>/', views.topic, name='topic')
]
