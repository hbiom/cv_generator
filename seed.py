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
Network.objects.all().delete()
Portfolio.objects.all().delete()


print("db deleted")

profile_test = "I'm a Life scientist passionate about the intersections of Healthcare and Data science and programming. \n\n During my thesis, I performed statistical and data visualization analysis on clinical and biological data (transcriptomic, flow cytometry) resulting in several scientific publications and oral presentations in international conferences. I also worked on machine learning projects applied to medical images and radiomics for classification and segmentation tasks. \n\n I have experience in back-end development (Python, SQL, Flask, Django) and front-end interface (HTML, CSS, JS). \n\nIm strongly motivated to work on projects aiming to have an impact on healthcare and clinical practice."

def seed():
  # hugo =  User.objects.get(username="hugo")

  hugo_profile = Profile.objects.create(
    first_name = "Hugo",
    last_name="Bottois",
    title =  "PhD",
    profile_pic = "https://res.cloudinary.com/dmeefs6iu/image/upload/v1626531093/public/images/avatar2_g5nxgg.jpg",
    about_me = profile_test,
    # user = hugo
  )

  Experience.objects.create(
  job_name = "Project Learder",
  company = "Capgemini Enginners",
  logo_company = "https://res.cloudinary.com/dmeefs6iu/image/upload/v1626531093/public/images/avatar2_g5nxgg.jpg",
  description =  profile_test,
  start_date = '2019-09-02',
  end_date = '2021-09-02',
  profile = hugo_profile
  )

  Experience.objects.create(
  job_name = "Project Learder",
  company = "Capgemini Enginners",
  logo_company = "https://res.cloudinary.com/dmeefs6iu/image/upload/v1626531093/public/images/avatar2_g5nxgg.jpg",
  description =  profile_test,
  start_date = '2019-09-02',
  end_date = '2021-09-02',
  profile = hugo_profile
  )

  programing = Skillcategory.objects.create(category_name="Programming")
  projet = Skillcategory.objects.create(category_name="Project")
  langue = Skillcategory.objects.create(category_name="Language")

  ML = Subcategory.objects.create(subcategory_name="Machine learning")
  Web = Subcategory.objects.create(subcategory_name="Web")

  # ML
  Skill.objects.create(name="Python",category=programing,subcategory=ML, profile = hugo_profile)
  Skill.objects.create(name="Sklearn",category=programing,subcategory=ML, profile = hugo_profile)
  Skill.objects.create(name="Keras",category=programing,subcategory=ML, profile = hugo_profile)
  Skill.objects.create(name="Tensorflow",category=programing,subcategory=ML, profile = hugo_profile)

  # Web
  HTML = Skill.objects.create(name="HTML",category=programing,subcategory=Web, profile = hugo_profile)
  CSS = Skill.objects.create(name="CSS",category=programing,subcategory=Web, profile = hugo_profile)
  Skill.objects.create(name="Javascript",category=programing,subcategory=Web, profile = hugo_profile)
  Skill.objects.create(name="Django",category=programing,subcategory=Web, profile = hugo_profile)
  Skill.objects.create(name="Flask",category=programing,subcategory=Web, profile = hugo_profile)

  Skill.objects.create(name="Project Managment",category=projet, profile = hugo_profile)
  Skill.objects.create(name="Trello",category=projet, profile = hugo_profile)
  Skill.objects.create(name="Communication",category=projet, profile = hugo_profile)

  Skill.objects.create(name="English",category=langue, profile = hugo_profile)
  Skill.objects.create(name="French",category=langue, profile = hugo_profile)

  Publication.objects.create(title = "Thesis : Acquisition and regulation of effector T cell functions in Crohn’s disease",
                             journal_name="Thesis",
                             publication_link="http://www.theses.fr/2019USPCC012",
                             author="Anne Caignard, Stéphane Nancey, Bertrand Meresse, Bottois Hugo, Claire Soudais, Lionel Le Bourhis, Matthieu Allez",
                             publication_date='2019-04-02',
                             profile = hugo_profile)

  Publication.objects.create(title = "Thesis : Acquisition and regulation of effector T cell functions in Crohn’s disease",
                             journal_name="Thesis",
                             publication_link="http://www.theses.fr/2019USPCC012",
                             author="Anne Caignard, Stéphane Nancey, Bertrand Meresse, Claire Soudais, Lionel Le Bourhis, Bottois Hugo, Matthieu Allez",
                             publication_date='2019-04-02',
                             profile = hugo_profile)

  Publication.objects.create(title = "Thesis : Acquisition and regulation of effector T cell functions in Crohn’s disease",
                             journal_name="Thesis",
                             publication_link="http://www.theses.fr/2019USPCC012",
                             author="Anne Caignard, Stéphane Nancey, Bottois Hugo, Bertrand Meresse, Claire Soudais, Lionel Le Bourhis, Matthieu Allez",
                             publication_date='2019-04-02',
                             profile = hugo_profile)


  Study.objects.create(img = "https://res.cloudinary.com/dmeefs6iu/image/upload/v1626531093/public/images/avatar2_g5nxgg.jpg",
                       school_name = "Bootcamp",
                       title= "Computer programming Bootcamp",
                       description= "24-week intensive coding bootcamp learning HTML, CSS, JavaScript, Ruby and Ruby on Rails, SQL, git, GitHub, deployement , project management, UI/UX" ,
                       obtention_date = '2019-04-02',
                       link = "https://www.lewagon.com/fr",
                       profile = hugo_profile )

  Study.objects.create(img = "https://res.cloudinary.com/dmeefs6iu/image/upload/v1626531093/public/images/avatar2_g5nxgg.jpg",
                       school_name = "Bootcamp",
                       title= "Computer programming Bootcamp",
                       description= "24-week intensive coding bootcamp learning HTML, CSS, JavaScript, Ruby and Ruby on Rails, SQL, git, GitHub, deployement , project management, UI/UX" ,
                       obtention_date = '2019-04-02',
                       link = "https://www.lewagon.com/fr",
                       profile = hugo_profile )

  Study.objects.create(img = "https://res.cloudinary.com/dmeefs6iu/image/upload/v1626531093/public/images/avatar2_g5nxgg.jpg",
                     school_name = "Bootcamp",
                     title= "Computer programming Bootcamp",
                     description= "24-week intensive coding bootcamp learning HTML, CSS, JavaScript, Ruby and Ruby on Rails, SQL, git, GitHub, deployement , project management, UI/UX" ,
                     obtention_date = '2019-04-02',
                     link = "https://www.lewagon.com/fr",
                     profile = hugo_profile )

  Network.objects.create(network_name = "linkedin", link="tkrtktk", profile=hugo_profile)
  Network.objects.create(network_name = "github", link="tkrtktk", profile=hugo_profile)
  Network.objects.create(network_name = "medium", link="tkrtktk", profile=hugo_profile)


  CTT = Portfolio.objects.create(project_title = "medium",
                           img="https://res.cloudinary.com/dmeefs6iu/image/upload/v1626531093/public/images/avatar2_g5nxgg.jpg",
                           description= 'zefoiz fjz vpizubevgoij evjbeor bbermore mv',
                           link_website="htt",
                           profile = hugo_profile
                           )
  CTT.skills.add(HTML, CSS)


  cursed = Portfolio.objects.create(project_title = "cursed",
                           img="https://res.cloudinary.com/dmeefs6iu/image/upload/v1626531093/public/images/avatar2_g5nxgg.jpg",
                           description= 'zefoiz fjz vpizubevgoij evjbeor bbermore mv',
                           link_website="htt",
                           profile = hugo_profile
                           )
  cursed.skills.add(HTML, CSS)



  print("seeding done")


seed()



