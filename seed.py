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

profile_description = "I'm a Life scientist passionate about the intersections of Healthcare and Data science and programming. \n\n During my thesis, I performed statistical and data visualization analysis on clinical and biological data (transcriptomic, flow cytometry) resulting in several scientific publications and oral presentations in international conferences. I also worked on machine learning projects applied to medical images and radiomics for classification and segmentation tasks. \n\n I have experience in back-end development (Python, SQL, Flask, Django) and front-end interface (HTML, CSS, JS). \n\nIm strongly motivated to work on projects aiming to have an impact on healthcare and clinical practice."

profile_test = "ezjovj jbvoij fedsorvb erosjeosrv mj vrfkje rzjgv zmkj zih g"

def seed():
  # hugo =  User.objects.get(username="hugo")

  hugo_profile = Profile.objects.create(
    first_name = "Hugo",
    last_name="Bottois",
    title =  "PhD",
    profile_pic = "https://res.cloudinary.com/dmeefs6iu/image/upload/v1626531093/public/images/avatar2_g5nxgg.jpg",
    about_me = profile_description
  )

  Capgemini = """ Developing diagnosis assistance for radiologist using machine learning applied on medical images
  \n\n
  Scientific Projects:
  \n\n
  - Classification of benign and malignant soft-tissue tumors based on images and radiomic data
  \n\n
  - Tumor Segmentation on osteosarcoma
  \n\n
  Development of a Web demonstrator to deploy our algorithm
  \n\n
  Mentoring intership and a team including data scientist and programmer
  \n\n
  Redaction and communication of scientific result
  \n\n
  Collaboration with biomedical imaging research laboratory CREATIS (Lyon)
  \n\n
  Technical track : Python, Numpy, Keras, Tensorflow, Sklearn, Nibabel, Django, Docker """

  Experience.objects.create(
  job_name = "Project Learder",
  company = "Capgemini Enginners",
  logo_company = "https://res.cloudinary.com/dmeefs6iu/image/upload/v1626531093/public/images/avatar2_g5nxgg.jpg",
  description =  Capgemini,
  start_date = '2019-09-02',
  end_date = '2021-09-02',
  profile = hugo_profile
  )

  inserm = """
    Thesis project: "Acquisition and regulation of effector T cells function in Crohn's disease"
    INSERM UMRS 1160 « microenvironment, lymphocyte development and homing»
    \n\n
    Scientific Projects:
    \n\n
    - Phenotypic and transcriptomic signature of CD8 tissue resident memory T cell subsets in healthy and Crohn's disease patient intestinal mucosa
    \n\n
    - Establishment of autologous co-coculture model of mucosal T cells and intestinal organoid to study lympho-epithelial interaction and T cell functions
    \n\n
    - Study of NKG2D receptor implication in Crohn's disease physiopathology
    \n\n
    Technical track : R, Bioconductor, Bioinformatic, Biostatistique, Flow cytometry, Organoid and Cell culture
  """

  Experience.objects.create(
  job_name = "Science project leader, PhD candidate",
  company = "Paris Diderot/Hopital Saint Louis",
  logo_company = "https://res.cloudinary.com/dmeefs6iu/image/upload/v1626531093/public/images/avatar2_g5nxgg.jpg",
  description =  inserm,
  start_date = '2015-09-02',
  end_date = '2019-04-03',
  profile = hugo_profile)

  programing = Skillcategory.objects.create(category_name="Programming")
  projet = Skillcategory.objects.create(category_name="Project")
  langue = Skillcategory.objects.create(category_name="Language")

  ML = Subcategory.objects.create(subcategory_name="Machine learning")
  Web = Subcategory.objects.create(subcategory_name="Web")

  # ML
  Python = Skill.objects.create(name="Python",category=programing,subcategory=ML, profile = hugo_profile)
  Sklearn = Skill.objects.create(name="Sklearn",category=programing,subcategory=ML, profile = hugo_profile)
  Keras = Skill.objects.create(name="Keras",category=programing,subcategory=ML, profile = hugo_profile)
  Tensorflow = Skill.objects.create(name="Tensorflow",category=programing,subcategory=ML, profile = hugo_profile)

  Matplotlib = Skill.objects.create(name="Matplotlib",category=programing,subcategory=ML, profile = hugo_profile)
  Numpy = Skill.objects.create(name="Numpy",category=programing,subcategory=ML, profile = hugo_profile)
  Nibabel = Skill.objects.create(name="Nibabel",category=programing,subcategory=ML, profile = hugo_profile)
  Heroku = Skill.objects.create(name="Heroku",category=programing,subcategory=ML, profile = hugo_profile)

  # Web
  ROR = Skill.objects.create(name="Ruby on rails",category=programing,subcategory=Web, profile = hugo_profile)
  Ruby = Skill.objects.create(name="Ruby",category=programing,subcategory=Web, profile = hugo_profile)
  HTML = Skill.objects.create(name="HTML",category=programing,subcategory=Web, profile = hugo_profile)
  CSS = Skill.objects.create(name="CSS",category=programing,subcategory=Web, profile = hugo_profile)
  JavaScript = Skill.objects.create(name="Javascript",category=programing,subcategory=Web, profile = hugo_profile)
  Django = Skill.objects.create(name="Django",category=programing,subcategory=Web, profile = hugo_profile)
  Flask = Skill.objects.create(name="Flask",category=programing,subcategory=Web, profile = hugo_profile)

  project_management = Skill.objects.create(name="Project Management",category=projet, profile = hugo_profile)
  Trello = Skill.objects.create(name="Trello",category=projet, profile = hugo_profile)
  Communication = Skill.objects.create(name="Communication",category=projet, profile = hugo_profile)

  English = Skill.objects.create(name="English",category=langue, profile = hugo_profile)
  French = Skill.objects.create(name="French",category=langue, profile = hugo_profile)


  Publication.objects.create(title = "Thesis : Acquisition and regulation of effector T cell functions in Crohn’s disease",
                             journal_name="Thesis",
                             publication_link="http://www.theses.fr/2019USPCC012",
                             author="Anne Caignard, Stéphane Nancey, Bertrand Meresse, Bottois Hugo, Claire Soudais, Lionel Le Bourhis, Matthieu Allez",
                             publication_date='2019-04-02',
                             profile = hugo_profile)

  Publication.objects.create(title = "KLRG1 and CD103 expressions define distinct intestinal tissue resident memory CD8 T cell subsets modulated in Crohn's Disease",
                             journal_name="Frontier of immunology",
                             publication_link="https://www.frontiersin.org/articles/10.3389/fimmu.2020.00896/full" ,
                             author="Hugo Bottois, Marjolaine Ngollo, Nassim Hammoudi, Tristan Courau,Julie Bonnereau, Victor Chardiny, Céline Grand, Brice Gergaud, Matthieu Allez, Lionel Le Bourhis",
                             publication_date='2020-05-12',
                             profile = hugo_profile)

  Publication.objects.create(title = "T cell clonal expansions in ileal Crohn's disease are associated with smoking behaviour and postoperative recurrence",
                             journal_name="Gut",
                             publication_link="https://gut.bmj.com/content/68/11/1961.abstract",
                             author="Allez M, Auzolle C, Ngollo M, Bottois H, Chardiny V, Corraliza AM, Salas A, Perez K, Stefanescu C, Nancey S, Buisson A, Pariente B, Fumery M, Sokol H, Tréton X1, Barnich N, Seksik P, Le Bourhis L; REMIND Study Group",
                             publication_date='2019-02-12',
                             profile = hugo_profile)


  Publication.objects.create(title = "Association Between Microscopic Lesions at Ileal Resection Margin and Recurrence After Surgery in Patients With Crohn’s Disease",
                             journal_name="Clinical Gastroenterology and Hepatology",
                             publication_link="https://www.cghjournal.org/article/S1542-3565(19)30435-5/pdft",
                             author="Nassim Hammoudi, Dominique Cazals-Hatem, Claire Auzolle, Charlotte Gardair, Marjolaine Ngollo, Hugo Bottois, Stéphane Nancey, Benjamin Pariente, Anthony Buisson, Xavier Treton, Mathurin Fumery, Madeleine Bezault, Philippe Seksik, Lionel Le Bourhis,REMIND Study Group Investigators , Jean-François Flejou, Matthieu Allez",
                             publication_date='2020-01-18',
                             profile = hugo_profile)


  Publication.objects.create(title = "Association Between Microscopic Lesions at Ileal Resection Margin and Recurrence After Surgery in Patients With Crohn’s Disease",
                             journal_name="Journal for ImmunoTherapy of cancer",
                             publication_link="https://jitc.biomedcentral.com/articles/10.1186/s40425-019-0553-9",
                             author="Tristan Courau, Julie Bonnereau, Justine Chicoteau, Hugo Bottois, Romain Remark,Laura Assante Miranda, Antoine Toubert, Mathieu Blery, Thomas Aparicio, Matthieu Allez, Lionel Le Bourhis",
                             publication_date='2019-03-14',
                             profile = hugo_profile)


  Publication.objects.create(title = "Crohn's Disease Mucosal Transcriptomes Highlight JAK/STAT Pathway Involvement in Postoperative Recurrence",
                             journal_name="Journal for ImmunoTherapy of cancer",
                             publication_link="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3439555",
                             author="Ngollo Marjolaine, Perez Kevin, Hammoudi Nassim, Gorelik Yuri, Delord Marc,Auzolle Claire, Bottois Hugo, Cazals-Hatem Dominique, Bezault Madeleine, Nancey Stéphane, Pariente Benjamin, Treton, Xavier, Fumery Mathurin, Anthony Buisson, Barnich Nicolas, Seksik Philippe, Investigators REMIND, Shen-Orr ShaiLe, Bourhis Lionel, Allez Matthieu",
                             publication_date='2019-08-22',
                             profile = hugo_profile)


  lewagon = """
  Attending Le Wagon Paris (Batch # 378):
  \n\n
  24-week intensive coding bootcamp learning HTML, CSS, JavaScript, Ruby and Ruby on Rails, SQL, git, GitHub, deployement , project management, UI/UX.
  /n/n
  Certification de Concepteur - Développeur d'applications web
  Enregistrée au RNCP au niveau VI (FR) et niveau VI (EU)
  Code NSF 326 informatique, traitement de l'information, réseaux de transmission
  """


  Study.objects.create(img = "https://res.cloudinary.com/dmeefs6iu/image/upload/v1626531093/public/images/avatar2_g5nxgg.jpg",
                       school_name = "Bootcamp",
                       title= "Computer programming Bootcamp",
                       description= lewagon,
                       obtention_date = '2019-04-02',
                       link = "https://www.lewagon.com/fr",
                       profile = hugo_profile )

  blent = """
    2 projects in collaboration with Datagram :
    \n\n
    Predict the consequences of a sale on the turnover :
    \n\n
    - Modeling and interpretation: Logistic Regression, CART, Random Forest, Gradient Boosting
    - Data Visualization
    Predict the category of a product based on its description:
    \n\n
    - NLP/word embedding/word2vec
    - Deep learning
    """

  Study.objects.create(img = "https://res.cloudinary.com/dmeefs6iu/image/upload/v1626531093/public/images/avatar2_g5nxgg.jpg",
                         school_name = "Blent.ai",
                         title= "Data science Bootcamp",
                         description= blent,
                         obtention_date = '2019-04-02',
                         link = "https://blent.ai/",
                         profile = hugo_profile )


  Study.objects.create(img = "https://res.cloudinary.com/dmeefs6iu/image/upload/v1626531093/public/images/avatar2_g5nxgg.jpg",
                         school_name = "University Paris Diderot",
                         title= "PhD, Immunology/biotherapy",
                         description= "Thesis project: \"Acquisition and regulation of effector T cells function in Crohn's disease\"\n\n Written and defended in English",
                         obtention_date = '2019-04-02',
                         link = "https://www.lewagon.com/fr",
                         profile = hugo_profile )


  Study.objects.create(img = "https://res.cloudinary.com/dmeefs6iu/image/upload/v1626531093/public/images/avatar2_g5nxgg.jpg",
                         school_name = "University Paris Diderot",
                         title= "Msc Science, Health and Application",
                         description= "Thesis project: \"Acquisition and regulation of effector T cells function in Crohn's disease\"\n\n Written and defended in English",
                         obtention_date = '2019-04-02',
                         link = "http://www.theses.fr/2019USPCC012",
                         profile = hugo_profile )


  dugbm = """
  This diploma is about the socio-economic and regulatory environment to valorize research and biomedical innovation coming from the hospital or the academic world in order to move towards real clinical application.
  \n\n
  Master memory : Algorithm based on molecular test to predict post-surgical clinical relapse from Crohn's disease patient.
  """


  Study.objects.create(img = "https://res.cloudinary.com/dmeefs6iu/image/upload/v1626531093/public/images/avatar2_g5nxgg.jpg",
                         school_name = "University Paris Pierre and Marie Curie",
                         title= "University Diploma",
                         description= dugbm,
                         obtention_date = '2019-04-02',
                         link = "https://dugbm.sorbonne-universite.fr/",
                         profile = hugo_profile )

  Study.objects.create(img = "https://res.cloudinary.com/dmeefs6iu/image/upload/v1626531093/public/images/avatar2_g5nxgg.jpg",
                         school_name = "University Le Havre",
                         title= "Bachelor of biology",
                         description= "",
                         obtention_date = '2019-04-02',
                         profile = hugo_profile )

  Network.objects.create(network_name = "linkedin", link="https://www.linkedin.com/in/hugo-bottois-phd-87aabb101/", profile=hugo_profile)
  Network.objects.create(network_name = "github", link="https://github.com/hbiom", profile=hugo_profile)
  Network.objects.create(network_name = "medium", link="https://hugobottois.medium.com/", profile=hugo_profile)


  CTT = Portfolio.objects.create(project_title = "Medical images visualization with python",
                           img="https://res.cloudinary.com/dmeefs6iu/image/upload/v1626531093/public/images/avatar2_g5nxgg.jpg",
                           description= 'Utilities for exploratory data analysis and visualization on nifti files (Colorectal cancer) with python',
                           link_medium="https://hugobottois.medium.com/medical-images-visualization-with-python-b40c2eb085f7",
                           link_github="https://github.com/hbiom/DataViz_CT_CCR",
                           profile = hugo_profile
                           )
  CTT.skills.add(Python, Matplotlib, Numpy, Nibabel)

  cursed = """
    ruby on rails application
    \n\n
    You can create an event and create/invite virtual fake users.
    \n\n
    Disponibilities for each invited user will be automaticaly created but no common date for all user will be found (like in the real word ...).
  """

  cursed = Portfolio.objects.create(project_title = "Doodle clone",
                           img="https://res.cloudinary.com/dmeefs6iu/image/upload/v1626531093/public/images/avatar2_g5nxgg.jpg",
                           description= cursed,
                           link_website="https://www.youtube.com/",
                           link_github="https://github.com/hbiom/DataViz_CT_CCR",
                           profile = hugo_profile
                           )
  cursed.skills.add(Ruby, ROR, HTML, CSS, JavaScript, Heroku)



  print("seeding done")


seed()

