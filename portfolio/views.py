from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib import messages

# ----------------------------
# Home Page - Auto Redirect
# ----------------------------
def home(request):
    return redirect('https://portfolio-website-vnav.onrender.com')


# ----------------------------
# About Page
# ----------------------------
def about_page(request):
    about = About.objects.first()
    skills = Skill.objects.all()
    social_links = SocialLink.objects.all()
    return render(request, 'main/about.html', {
        'about': about,
        'social_links': social_links,
        'skills': skills
    })


# ----------------------------
# Projects Page
# ----------------------------
def projects_page(request):
    projects = Project.objects.all()
    return render(request, 'main/projects.html', {
        'projects': projects,
    })


# ----------------------------
# Single Project Page
# ----------------------------
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    images = project.images.all()
    return render(request, 'main/project_detail.html', {
        'project': project,
        'images': images,
    })


# ----------------------------
# Blog Page
# ----------------------------
def blog_list(request):
    blogs = BlogPost.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'main/blog.html', {
        'blogs': blogs,
    })


# ----------------------------
# Blog Detail
# ----------------------------
def blog_detail(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    images = blog.images.all()
    return render(request, 'main/blog_detail.html', {
        'blog': blog,
        'images': images,
    })


# ----------------------------
# Certifications Page
# ----------------------------
def certifications_page(request):
    certifications = Certification.objects.all().order_by('-date')
    return render(request, 'main/certifications.html', {
        'certifications': certifications,
    })


# ----------------------------
# Contact Page + Form Submission
# ----------------------------
def contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_text = request.POST.get('message')
        
        if name and email and message_text:
            Message.objects.create(name=name, email=email, message=message_text)
            messages.success(request, 'Message sent successfully!')
        else:
            messages.error(request, 'Please fill all fields.')

        return redirect('contact')

    social_links = SocialLink.objects.all()
    return render(request, 'main/contact.html', {
        'social_links': social_links
    })
