from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    """Homepage app Knowledge Base"""
    return render(request, 'knowledge_logs/index.html')

def topics(request):
    """Show topic list"""
    topics = Topic.objects.order_by('date_added')
    content = {'topics': topics}
    return render(request, 'knowledge_logs/topics.html', content)

def topic(request, topic_id):
    """Show one topic and all notice"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'knowledge_logs/topic.html', context)
