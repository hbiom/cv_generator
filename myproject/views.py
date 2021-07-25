from django.shortcuts import render
from mycv.models import *
from utility import diplay_skills

def home(request):
  profiles = Profile.objects.all()
  experiences = Experience.objects.all()
  skillcategories = Skillcategory.objects.all()
  skills = Skill.objects.all()
  publications = Publication.objects.all()
  studies = Study.objects.all()

  skills_dico = diplay_skills(skillcategories, Subcategory.objects.all(), skills)

  return render(request, 'home.html',{'experiences':experiences,"profiles":profiles,
    "skillcategories":skillcategories,'skills':skills,'publications':publications,"skills_dico":skills_dico})



