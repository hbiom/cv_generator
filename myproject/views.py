from django.shortcuts import render
from mycv.models import *

def home(request):
  profile = Profile.objects.all()
  experiences = Experience.objects.all()
  skills = Skill.objects.all()
  publications = Publication.objects.all()
  studies = Study.objects.all()

  return render(request, 'home.html',{'experiences':experiences})



