import os
from datetime import date
from django.db import models
import django
from django.db.models import DateTimeField
from django.contrib import auth
import datetime
from datetime import timedelta
import cloudinary
from cloudinary.models import CloudinaryField


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

django.setup()

from mycv.models import *
from django.contrib.auth.models import User


Profile.objects.all().delete()
Experience.objects.all().delete()
Skill.objects.all().delete()
Skillcategory.objects.all().delete()
Subcategory.objects.all().delete()

print("db deleted")

profile_test = "Im a Life scientist passionate about the intersections of Healthcare and Data science and programming. During my thesis, I performed statistical and data visualization analysis on clinical and biological data (transcriptomic, flow cytometry) resulting in several scientific publications and oral presentations in international conferences. I also worked on machine learning projects applied to medical images and radiomics for classification and segmentation tasks. I have experience in back-end development (Python, SQL, Flask, Django) and front-end interface (HTML, CSS, JS).Im strongly motivated to work on projects aiming to have an impact on healthcare and clinical practice."

def seed():
  hugo =  User.objects.get(username="hbottois")

  Profile.objects.create(
    first_name = "Hugo",
    last_name="Bottois",
    title =  "PhD",
    profile_pic = "https://res.cloudinary.com/dmeefs6iu/image/upload/v1626531093/public/images/avatar2_g5nxgg.jpg",
    about_me = profile_test,
    user = hugo
  )
  Experience.objects.create(
  job_name = "Project Learder",
  company = "Capgemini Enginners",
  logo_company = "https://res.cloudinary.com/dmeefs6iu/image/upload/v1626531093/public/images/avatar2_g5nxgg.jpg",
  description =  profile_test,
  start_date = '2019-09-02',
  end_date = '2021-09-02',
  user = hugo
  )

  Experience.objects.create(
  job_name = "Project Learder",
  company = "Capgemini Enginners",
  logo_company = "https://res.cloudinary.com/dmeefs6iu/image/upload/v1626531093/public/images/avatar2_g5nxgg.jpg",
  description =  profile_test,
  start_date = '2019-09-02',
  end_date = '2021-09-02',
  user = hugo
  )

  programing = Skillcategory.objects.create(category_name="Programming")
  projet = Skillcategory.objects.create(category_name="Project")
  langue = Skillcategory.objects.create(category_name="Language")


  ML = Subcategory.objects.create(subcategory_name="Machine learning")
  Web = Subcategory.objects.create(subcategory_name="Web")

  Skill.objects.create(name="Python",category=programing,Subcategory=ML)
  Skill.objects.create(name="HTML",category=programing,Subcategory=ML)
  Skill.objects.create(name="CSS",category=programing,Subcategory=Web)
  Skill.objects.create(name="Javascript",category=programing,Subcategory=Web)
  Skill.objects.create(name="Django",category=programing,Subcategory=Web)
  Skill.objects.create(name="Flask",category=programing,Subcategory=Web)

  Skill.objects.create(name="Project Managment",category=projet)
  Skill.objects.create(name="Trello",category=projet)
  Skill.objects.create(name="Communication",category=projet)

  Skill.objects.create(name="English",category=langue)
  Skill.objects.create(name="French",category=langue)
  Skill.objects.create(name="Portuguese",category=langue)

  print("done")


seed()

