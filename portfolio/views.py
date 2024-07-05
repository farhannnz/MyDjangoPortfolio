
# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Skill, Education, Project
from .forms import MessageForm

def home(request):
    skills = Skill.objects.all()
    return render(request, 'portfolio/home.html', {'skills': skills})

def education(request):
    educations = Education.objects.all()
    return render(request, 'portfolio/education.html', {'educations': educations})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})

def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'portfolio/contact_success.html')
    else:
        form = MessageForm()
    return render(request, 'portfolio/contact.html', {'form': form})
