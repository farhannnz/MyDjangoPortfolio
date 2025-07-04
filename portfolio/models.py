from django.db import models

# ----------------------------
# Skills
# ----------------------------
class Skill(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='skill/')

    def __str__(self):
        return self.name


# ----------------------------
# Projects with Multiple Images
# ----------------------------
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    visit_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return f"Image for {self.project.title}"


# ----------------------------
# Blog
# ----------------------------
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class BlogImage(models.Model):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='blogs/')

    def __str__(self):
        return f"Image for {self.blog.title}"


# ----------------------------
# Message (Contact Form)
# ----------------------------
class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


# ----------------------------
# About Section
# ----------------------------
class About(models.Model):
    heading = models.CharField(max_length=200, default='About Me')
    content = models.TextField()
    profile_image = models.ImageField(upload_to='about/', blank=True, null=True)

    def __str__(self):
        return "About Section"


# ----------------------------
# Certifications
# ----------------------------
class Certification(models.Model):
    title = models.CharField(max_length=200)
    issued_by = models.CharField(max_length=200)
    date = models.DateField()
    certificate_image = models.ImageField(upload_to='certificates/', blank=True, null=True)
    certificate_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


# ----------------------------
# Social Media Links
# ----------------------------
class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ('linkedin', 'LinkedIn'),
        ('github', 'GitHub'),
        ('twitter', 'Twitter'),
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook'),
        ('website', 'Website'),
        # aur bhi add kar sakta hai
    ]

    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    url = models.URLField()
    icon_image = models.ImageField(upload_to='social_icons/')

    def __str__(self):
        return self.platform

