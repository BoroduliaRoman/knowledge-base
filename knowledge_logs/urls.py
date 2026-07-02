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
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
]
