from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm

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

def new_topic(request):
    """Define new topic"""
    if request.method != 'POST':
        # Data wasn't sent; Create new form
        form = TopicForm()
    else:
        # Data was send 'POST'; Proceed the data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('knowledge_logs:topics')

    # Show empty or isn't valid form
    context = {'form': form}
    return render(request, 'knowledge_logs/new_topic.html', context)
