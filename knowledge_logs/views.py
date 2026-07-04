from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
    """Homepage app Knowledge Base"""
    return render(request, 'knowledge_logs/index.html')

@login_required
def topics(request):
    """Show topic list"""
    topics = Topic.objects.order_by('date_added')
    content = {'topics': topics}
    return render(request, 'knowledge_logs/topics.html', content)

@login_required
def topic(request, topic_id):
    """Show one topic and all notice"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'knowledge_logs/topic.html', context)

@login_required
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

@login_required
def new_entry(request, topic_id):
    """Adding new entry by topic"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # Data wasn't sent; Create new form
        form = EntryForm()
    else:
        # Data was send 'POST'; Proceed the data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('knowledge_logs:topic', topic_id=topic_id)

    # Show empty or isn't valid form
    content = {'topic': topic, 'form': form}
    return render(request, 'knowledge_logs/new_entry.html', content)

@login_required
def edit_entry(request, entry_id):
    """Edit exist entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Current request; form fill data current entry
        form = EntryForm(instance=entry)
    else:
        # Send data POST; Processing data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('knowledge_logs:topic', topic_id=topic.id)

    content = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'knowledge_logs/edit_entry.html', content)