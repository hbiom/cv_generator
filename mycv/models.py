
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=80)
  last_name = models.CharField(max_length=80)
  title = models.CharField(max_length=80)
  profile_pic = cloudinary.models.CloudinaryField('image')
  about_me =  models.TextField(max_length=800)


  def full_name(self):
    ''' return full name of profile user'''
    return f'{self.last_name.capitalize() } {self.first_name.capitalize() }'


class Experience(models.Model):
  job_name = models.CharField(max_length=100)
  company = models.CharField(max_length=100)
  logo_company = cloudinary.models.CloudinaryField('image')
  description =  models.TextField(max_length=800)
  start_date = models.DateField()
  end_date = models.DateField()
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

class Skillcategory(models.Model):
  category_name = models.CharField(max_length=150)

class Subcategory(models.Model):
  subcategory_name = models.CharField(max_length=150)

class Skill(models.Model):
  name = models.CharField(max_length=150)
  category = models.ForeignKey(Skillcategory, on_delete=models.CASCADE)
  subcategory = models.ForeignKey(Subcategory, blank=True, null=True, on_delete=models.CASCADE)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

class Publication(models.Model):
  title = models.CharField(max_length=80)
  journal_name = models.CharField(max_length=150)
  publication_link = models.URLField(max_length=10000)
  author =  models.TextField(max_length=800)
  abstract =  models.TextField(max_length=800, null=True)
  publication_date = models.DateField()
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

class Study(models.Model):
  img = cloudinary.models.CloudinaryField('image')
  school_name = models.CharField(max_length=300, null=True)
  title = models.CharField(max_length=80)
  description =  models.TextField(max_length=800, null=True)
  obtention_date = models.DateField()
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
  link = models.CharField(max_length=500, null=True)


NETWORK = (
  ("linkedin", "linkedin"),
  ("twitter", "twitter"),
  ("github", "github"),
  ("medium", "medium"),
)

class Network(models.Model):
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
  network_name = models.CharField(max_length=100, choices=NETWORK)
  link = models.CharField(max_length=500, null=True)



