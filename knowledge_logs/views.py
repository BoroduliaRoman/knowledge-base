from django.shortcuts import render

# Create your views here.

def index(request):
    """Homepage app Knowledge Base"""
    return render(request, 'knowledge_logs/index.html')
