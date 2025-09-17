from django.contrib import admin
from .models import PersonalInfo, Education, Experience, Project, Research, SkillCategory, Activity

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'location']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['institution', 'degree', 'start_date', 'end_date', 'order']
    list_editable = ['order']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['company', 'position', 'start_date', 'end_date', 'order']
    list_editable = ['order']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'technologies', 'order']
    list_editable = ['order']

@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):
    list_display = ['title', 'professor', 'date', 'order']
    list_editable = ['order']

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['description', 'order']
    list_editable = ['order']
