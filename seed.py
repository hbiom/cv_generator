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


def seed():
  hugo =  User.objects.get(username="hbottois")

  profile = Profile.objects.create(
    first_name = "Hugo",
    last_name="Bottois",
    title =  "PhD",
    profile_pic = "https://res.cloudinary.com/dmeefs6iu/image/upload/v1626531093/public/images/avatar2_g5nxgg.jpg",
    about_me = "ee szkcncùklj vcoẑejdnvc ojz voẑev ozrenvonzvoikn ",
    user = hugo
  )
  print("done")


seed()
