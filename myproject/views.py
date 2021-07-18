from django.shortcuts import render
from mycv.models import *

def home(request):
  profiles = Profile.objects.all()
  experiences = Experience.objects.all()
  skillCategories = SkillCategory.objects.all()
  skills = Skill.objects.all()
  publications = Publication.objects.all()
  studies = Study.objects.all()

  return render(request, 'home.html',{'experiences':experiences,"profiles":profiles,"skillCategories":skillCategories,'skills':skills})



