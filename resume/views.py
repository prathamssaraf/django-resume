from django.shortcuts import render
from .models import PersonalInfo, Education, Experience, Project, Research, SkillCategory, Activity

def resume_view(request):
    context = {
        'personal_info': PersonalInfo.objects.first(),
        'education': Education.objects.all(),
        'experience': Experience.objects.all(),
        'projects': Project.objects.all(),
        'research': Research.objects.all(),
        'skill_categories': SkillCategory.objects.all(),
        'activities': Activity.objects.all(),
    }
    return render(request, 'resume/resume.html', context)
