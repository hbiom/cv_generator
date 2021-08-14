
# Create your models here.
from django.db import models
# from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField

class Profile(models.Model):
  # user = models.OneToOneField(User, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=80)
  last_name = models.CharField(max_length=80)
  title = models.CharField(max_length=200)
  profile_pic = cloudinary.models.CloudinaryField('image')
  about_me =  models.TextField(max_length=4000)

  def full_name(self):
    ''' return full name of profile user'''
    return f'{self.last_name.capitalize() } {self.first_name.capitalize() }'

  def __str__(self):
      return self.first_name + " " + self.last_name

class Skillcategory(models.Model):
  category_name = models.CharField(max_length=150)

  def __str__(self):
    return self.category_name

class Subcategory(models.Model):
  subcategory_name = models.CharField(max_length=150)

  def __str__(self):
    return self.subcategory_name

class Skill(models.Model):
  name = models.CharField(max_length=150)
  category = models.ForeignKey(Skillcategory,blank=True, null=True, on_delete=models.CASCADE)
  subcategory = models.ForeignKey(Subcategory, blank=True, null=True, on_delete=models.CASCADE)
  core_skill = models.BooleanField(default=False)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

class Experience(models.Model):
  job_name = models.CharField(max_length=100)
  company = models.CharField(max_length=100)
  logo_company = cloudinary.models.CloudinaryField('image')
  description =  models.TextField(max_length=4000)
  start_date = models.DateField()
  end_date = models.DateField()
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
  skills = models.ManyToManyField(Skill)

  def __str__(self):
    return self.job_name

class Publication(models.Model):
  title = models.CharField(max_length=250)
  journal_name = models.CharField(max_length=150)
  publication_link = models.URLField(max_length=10000)
  author =  models.TextField(max_length=4000)
  abstract =  models.TextField(max_length=4000, null=True)
  publication_date = models.DateField()
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

  def __str__(self):
    return self.title


class Study(models.Model):
  img = cloudinary.models.CloudinaryField('image')
  school_name = models.CharField(max_length=300, null=True)
  title = models.CharField(max_length=250)
  description =  models.TextField(max_length=4000, null=True)
  obtention_date = models.DateField()
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
  link = models.URLField(max_length=500, null=True)

  def __str__(self):
    return self.title

NETWORK = (
  ("linkedin", "linkedin"),
  ("twitter", "twitter"),
  ("github", "github"),
  ("medium", "medium"),
)

class Network(models.Model):
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
  network_name = models.CharField(max_length=100, choices=NETWORK)
  link = models.URLField(max_length=500, null=True)

  def __str__(self):
    return self.network_name

class Portfolio(models.Model):
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
  img = cloudinary.models.CloudinaryField('image')
  skills = models.ManyToManyField(Skill)
  project_title = models.CharField(max_length=250)
  description =  models.TextField(max_length=4000)
  link_website = models.URLField(max_length=1500, null=True)
  link_github = models.URLField(max_length=1500, null=True)
  link_medium = models.URLField(max_length=1500, null=True)

  def __str__(self):
    return self.project_title
