from django.shortcuts import render, get_object_or_404
from mycv.models import *
from utility import diplay_skills

def profile(request,profile_id):

  user = get_object_or_404(User, pk=profile_id)
  profile = get_object_or_404(Profile, pk=user.profile.id)

  experiences = Experience.objects.filter(profile=profile)
  publications = Publication.objects.filter(profile=profile)
  studies = Study.objects.filter(profile=profile)
  skills = Skill.objects.filter(profile=profile)

  # optimize query (select the one linked to profile)
  subcategories = Subcategory.objects.all()
  skillcategories = Skillcategory.objects.all()
  networks = Network.objects.all()

  skills_dico = diplay_skills(skillcategories, subcategories, skills)

  return render(request, 'profile.html',{'experiences':experiences,"profile":profile,
    'skills':skills,'publications':publications,"networks":networks,"skills_dico":skills_dico,"studies":studies})


