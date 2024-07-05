
# Register your models here.
from django.contrib import admin
from .models import Skill, Education, Project, Message

admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Message)
