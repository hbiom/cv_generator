
# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=80)
  last_name = models.CharField(max_length=80)
  title = models.CharField(max_length=80)
  profile_pic = models.ImageField(upload_to='images/')
  about_me =  models.TextField(max_length=800)

class Experience(models.Model):
  job_name = models.CharField(max_length=100)
  company = models.CharField(max_length=100)
  logo_company = models.ImageField(upload_to='images/')
  description =  models.TextField(max_length=800)

  start_date = models.DateField()
  end_date = models.DateField()

  User = models.ForeignKey(User, on_delete=models.CASCADE)


class SkillCategory(models.Model):
  category = models.CharField(max_length=150)
  User = models.ForeignKey(User, on_delete=models.CASCADE)


class Skill(models.Model):
  name = models.CharField(max_length=150)
  category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)


class Publication(models.Model):
  title = models.CharField(max_length=80)
  journal_name = models.CharField(max_length=150)
  publication_link = models.URLField(max_length=10000)
  Author =  models.TextField(max_length=800)
  abstract =  models.TextField(max_length=800, null=True)
  publication_date = models.DateField()
  category = models.ForeignKey(User, on_delete=models.CASCADE)


class Study(models.Model):
  institut = models.ImageField(upload_to='images/')
  title = models.CharField(max_length=80)
  description =  models.TextField(max_length=800, null=True)
  obtention_date = models.DateField()


