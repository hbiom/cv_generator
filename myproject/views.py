from django.shortcuts import render, get_object_or_404
from mycv.models import *
from utility import diplay_skills
import re



def profil(request):

  try:
    profile = Profile.objects.exists()
  except Profile.DoesNotExist:
    return render(request, 'profile.html')

  profile = Profile.objects.all().first()

  experiences = Experience.objects.filter(profile=profile)
  publications = Publication.objects.filter(profile=profile)
  studies = Study.objects.filter(profile=profile)
  skills = Skill.objects.filter(profile=profile, core_skill=True)
  portfolios = Portfolio.objects.filter(profile=profile)

  # optimize query (select the one linked to profile)
  subcategories = Subcategory.objects.all()
  skillcategories = Skillcategory.objects.all()
  networks = Network.objects.all()

  skills_dico = diplay_skills(skillcategories, subcategories, skills)

  return render(request, 'profile.html',{'experiences':experiences,"profile":profile,
    'skills':skills,'publications':publications,"networks":networks,"skills_dico":skills_dico,
    "studies":studies,'portfolios':portfolios})

