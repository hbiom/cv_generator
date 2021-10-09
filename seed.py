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

profile_description = "I'm a Life scientist passionate about the intersections of Healthcare and Data science and programming.  <br><br> During my thesis, I performed statistical and data visualization analysis on clinical and biological data (transcriptomic, flow cytometry) resulting in several scientific publications and oral presentations in international conferences. I also worked on machine learning projects applied to medical images and radiomics for classification and segmentation tasks.  <br><br> I have experience in back-end development (Python, SQL, Flask, Django) and front-end interface (HTML, CSS, JS).  <br><br> Im strongly motivated to work on projects aiming to have an impact on healthcare and clinical practice."


def seed():

  hugo_profile = Profile.objects.create(
    first_name = "Hugo",
    last_name="Bottois",
    title =  "PhD",
    profile_pic = "https://res.cloudinary.com/dmeefs6iu/image/upload/v1626531093/public/images/avatar2_g5nxgg.jpg",
    about_me = profile_description
  )

  programing = Skillcategory.objects.create(category_name="Programming")
  projet = Skillcategory.objects.create(category_name="Project")
  langue = Skillcategory.objects.create(category_name="Language")
  LF = Skillcategory.objects.create(category_name="Life science")

  ML = Subcategory.objects.create(subcategory_name="Machine learning")
  Web = Subcategory.objects.create(subcategory_name="Web")

  # ML
  Python = Skill.objects.create(name="Python",category=programing,subcategory=ML, profile = hugo_profile, core_skill = True)
  Sklearn = Skill.objects.create(name="Sklearn",category=programing,subcategory=ML, profile = hugo_profile, core_skill = True)
  Keras = Skill.objects.create(name="Keras",category=programing,subcategory=ML, profile = hugo_profile, core_skill = True)
  Tensorflow = Skill.objects.create(name="Tensorflow",category=programing,subcategory=ML, profile = hugo_profile, core_skill = True)

  Matplotlib = Skill.objects.create(name="Matplotlib",category=programing,subcategory=ML, profile = hugo_profile)
  Seaborn = Skill.objects.create(name="Seaborn",category=programing,subcategory=ML, profile = hugo_profile)
  Numpy = Skill.objects.create(name="Numpy",category=programing,subcategory=ML, profile = hugo_profile)
  Nibabel = Skill.objects.create(name="Nibabel",category=programing,subcategory=ML, profile = hugo_profile)
  Heroku = Skill.objects.create(name="Heroku",category=programing,subcategory=ML, profile = hugo_profile)

  # Web
  ROR = Skill.objects.create(name="Ruby on rails",category=programing,subcategory=Web, profile = hugo_profile)
  Ruby = Skill.objects.create(name="Ruby",category=programing,subcategory=Web, profile = hugo_profile)
  HTML = Skill.objects.create(name="HTML",category=programing,subcategory=Web, profile = hugo_profile, core_skill = True)
  CSS = Skill.objects.create(name="CSS",category=programing,subcategory=Web, profile = hugo_profile, core_skill = True)
  JavaScript = Skill.objects.create(name="Javascript",category=programing,subcategory=Web, profile = hugo_profile, core_skill = True)
  Django = Skill.objects.create(name="Django",category=programing,subcategory=Web, profile = hugo_profile, core_skill = True)
  Flask = Skill.objects.create(name="Flask",category=programing,subcategory=Web, profile = hugo_profile, core_skill = True)

  project_management = Skill.objects.create(name="Project Management",category=projet, profile = hugo_profile, core_skill = True)
  Trello = Skill.objects.create(name="Trello",category=projet, profile = hugo_profile, core_skill = True)
  Communication = Skill.objects.create(name="Communication",category=projet, profile = hugo_profile, core_skill = True)

  English = Skill.objects.create(name="English",category=langue, profile = hugo_profile, core_skill = True)
  French = Skill.objects.create(name="French",category=langue, profile = hugo_profile, core_skill = True)


  # Life science
  R = Skill.objects.create(name="R",category=LF, profile = hugo_profile)
  Immunology = Skill.objects.create(name="Immunology",category=LF, profile = hugo_profile, core_skill = True)
  Cancer = Skill.objects.create(name="Cancer",category=LF, profile = hugo_profile, core_skill = True)
  Bioinformatic = Skill.objects.create(name="Bioinformatic",category=LF, profile = hugo_profile, core_skill = True)
  Bioconductor = Skill.objects.create(name="Bioconductor",category=LF, profile = hugo_profile, core_skill = True)
  Biostatistique = Skill.objects.create(name="Biostatistic",category=LF, profile = hugo_profile, core_skill = True)
  Flow_cytometry = Skill.objects.create(name="Flow cytometry",category=LF, profile = hugo_profile, core_skill = True)
  Organoid = Skill.objects.create(name="Organoid",category=LF, profile = hugo_profile, core_skill = True)
  Cell_culture = Skill.objects.create(name="Cell culture",category=LF, profile = hugo_profile, core_skill = True)


  Capgemini_text = """ Developing diagnosis assistance for radiologist using machine learning applied on medical images
  <br><br>
  <b>Scientific Projects:</b>
  <br><br>
  - Classification of benign and malignant soft-tissue tumors based on images and radiomic data
  <br><br>
  - Tumor Segmentation on osteosarcoma
  <br><br>
  - Development of Rest API and Web application to deploy machine learning solution
  <br><br>
  - Mentoring intership and a team including data scientist and programmer
  <br><br>
  - Redaction and communication of scientific result
  <br><br>
  - Collaboration with biomedical imaging research laboratory CREATIS (Lyon)
  <br><br>
  """

  Capgemini = Experience.objects.create(
                                        job_name = "Project leader",
                                        company = "Capgemini engineering",
                                        logo_company = "https://res.cloudinary.com/dmeefs6iu/image/upload/v1628965171/n8jfbgljjyhird1szzyn.png",
                                        description =  Capgemini_text,
                                        start_date = '2019-09-02',
                                        end_date = '2021-09-02',
                                        profile = hugo_profile)

  inserm_text = """
    Thesis project: "Acquisition and regulation of effector T cells function in Crohn's disease"
    INSERM UMRS 1160 « microenvironment, lymphocyte development and homing»
    <br><br>
    <b>Scientific Projects:</b>
    <br><br>
    - Phenotypic and transcriptomic signature of CD8 tissue resident memory T cell subsets in healthy and Crohn's disease patient intestinal mucosa
    <br><br>
    - Establishment of autologous co-coculture model of mucosal T cells and intestinal organoid to study lympho-epithelial interaction and T cell functions
    <br><br>
    - Study of NKG2D receptor implication in Crohn's disease physiopathology
    <br><br>
  """

  inserm = Experience.objects.create(
                                    job_name = "Science project leader, PhD candidate",
                                    company = "Paris Diderot/Hopital Saint Louis",
                                    logo_company = "https://res.cloudinary.com/dmeefs6iu/image/upload/v1628965190/b14buodzeezqwxbdh9xd.png",
                                    description =  inserm_text,
                                    start_date = '2015-09-02',
                                    end_date = '2019-04-03',
                                    profile = hugo_profile)


  Capgemini.skills.add(Python, Matplotlib, Numpy, Nibabel, Keras, Sklearn, Nibabel, Django, Flask)
  inserm.skills.add(R, Bioconductor, Bioinformatic, Biostatistique, Flow_cytometry, Organoid, Cell_culture)




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
                             publication_link="https://pubmed.ncbi.nlm.nih.gov/31042575/",
                             author="Nassim Hammoudi, Dominique Cazals-Hatem, Claire Auzolle, Charlotte Gardair, Marjolaine Ngollo, Hugo Bottois, Stéphane Nancey, Benjamin Pariente, Anthony Buisson, Xavier Treton, Mathurin Fumery, Madeleine Bezault, Philippe Seksik, Lionel Le Bourhis, REMIND Study Group Investigators , Jean-François Flejou, Matthieu Allez",
                             publication_date='2020-01-18',
                             profile = hugo_profile)


  Publication.objects.create(title = "Cocultures of human colorectal tumor spheroids with immune cells reveal the therapeutic potential of MICA/B and NKG2A targeting for cancer treatment",
                             journal_name="Journal for ImmunoTherapy of cancer",
                             publication_link="https://jitc.biomedcentral.com/articles/10.1186/s40425-019-0553-9",
                             author="Tristan Courau, Julie Bonnereau, Justine Chicoteau, Hugo Bottois, Romain Remark,Laura Assante Miranda, Antoine Toubert, Mathieu Blery, Thomas Aparicio, Matthieu Allez, Lionel Le Bourhis",
                             publication_date='2019-03-14',
                             profile = hugo_profile)


  Publication.objects.create(title = "Crohn's Disease Mucosal Transcriptomes Highlight JAK/STAT Pathway Involvement in Postoperative Recurrence",
                             journal_name="The Lancet (preprint)",
                             publication_link="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3439555",
                             author="Ngollo Marjolaine, Perez Kevin, Hammoudi Nassim, Gorelik Yuri, Delord Marc, Auzolle Claire, Bottois Hugo, Cazals-Hatem Dominique, Bezault Madeleine, Nancey Stéphane, Pariente Benjamin, Treton, Xavier, Fumery Mathurin, Anthony Buisson, Barnich Nicolas, Seksik Philippe, Investigators REMIND, Shen-Orr ShaiLe, Bourhis Lionel, Allez Matthieu",
                             publication_date='2019-08-22',
                             profile = hugo_profile)



  Publication.objects.create(title = "Radiomics vs Deep Learning to predict lipomatous soft tissue tumors malignancy on Magnetic Resonance Imaging",
                             journal_name="Experimental journal of radiology (under review)",
                             publication_link="",
                             author="",
                             publication_date='2021-01-01',
                             profile = hugo_profile)


  lewagon = """
  Attending Le Wagon Paris (Batch # 378):
  <br><br>
  24-week intensive coding bootcamp learning HTML, CSS, JavaScript, Ruby and Ruby on Rails, SQL, git, GitHub, deployement , project management, UI/UX.
  <br><br>
  Certification de Concepteur - Développeur d'applications web
  Enregistrée au RNCP au niveau VI (FR) et niveau VI (EU)
  Code NSF 326 informatique, traitement de l'information, réseaux de transmission
  """


  Study.objects.create(img = "https://res.cloudinary.com/dmeefs6iu/image/upload/v1628966624/lewagon_tsnchh.png",
                       school_name = "Lewagon",
                       title= "Computer programming",
                       description= lewagon,
                       obtention_date = '2019-04-02',
                       link = "https://www.lewagon.com/fr",
                       profile = hugo_profile )

  blent = """
    2 projects in collaboration with Datagram :
    <br><br>
    Predict the consequences of a sale on the turnover :
    <br><br>
    - Modeling and interpretation: Logistic Regression, CART, Random Forest, Gradient Boosting
    - Data Visualization
    Predict the category of a product based on its description:
    <br><br>
    - NLP/word embedding/word2vec
    <br><br>
    - Deep learning
    """

  Study.objects.create(img = "https://res.cloudinary.com/dmeefs6iu/image/upload/v1628966624/blent_rdh8rg.jpg",
                         school_name = "Blent.ai",
                         title= "Data science Bootcamp",
                         description= blent,
                         obtention_date = '2019-04-02',
                         link = "https://blent.ai/",
                         profile = hugo_profile )


  Study.objects.create(img = "https://res.cloudinary.com/dmeefs6iu/image/upload/v1628966624/paris7_logo_bit4fu.png",
                         school_name = "University Paris Diderot",
                         title= "Thesis in Immunology/Biotherapy",
                         description= "Thesis project: \"Acquisition and regulation of effector T cells function in Crohn's disease\"\n\n Written and defended in English",
                         obtention_date = '2019-04-02',
                         link = "https://www.lewagon.com/fr",
                         profile = hugo_profile )



  Study.objects.create(img = "https://res.cloudinary.com/dmeefs6iu/image/upload/v1628966624/paris7_logo_bit4fu.png",
                     school_name = "University Paris Diderot",
                     title= "Msc Science, Health and Application",
                     description= "",
                     obtention_date = '2016-09-02',
                     link = "https://www.lewagon.com/fr",
                     profile = hugo_profile )

  dugbm = """
  This diploma is about the socio-economic and regulatory environment to valorize research and biomedical innovation coming from the hospital or the academic world in order to move towards real clinical application.
  <br><br>
  Master memory : Algorithm based on molecular test to predict post-surgical clinical relapse from Crohn's disease patient.
  """


  Study.objects.create(img = "https://res.cloudinary.com/dmeefs6iu/image/upload/v1628966624/upmc_vhr9l1.png",
                         school_name = "University Paris Pierre and Marie Curie",
                         title= "University Diploma",
                         description= dugbm,
                         obtention_date = '2019-04-02',
                         link = "https://dugbm.sorbonne-universite.fr/",
                         profile = hugo_profile )

  # Study.objects.create(img = "https://res.cloudinary.com/dmeefs6iu/image/upload/v1628966623/lehavre_logo_kx3liu.png",
  #                        school_name = "University Le Havre",
  #                        title= "Bachelor of biology",
  #                        description= "",
  #                        obtention_date = '2019-04-02',
  #                        profile = hugo_profile )

  Network.objects.create(network_name = "linkedin", link="https://www.linkedin.com/in/hugo-bottois-phd-87aabb101/", profile=hugo_profile)
  Network.objects.create(network_name = "github", link="https://github.com/hbiom", profile=hugo_profile)
  Network.objects.create(network_name = "medium", link="https://hugobottois.medium.com/", profile=hugo_profile)




  CTT = Portfolio.objects.create(project_title = "Medical images visualization with python",
                           img="https://res.cloudinary.com/dmeefs6iu/image/upload/v1628965520/mxikal01ilghvqrk4lmx.png",
                           description= 'Utilities for exploratory data analysis and visualization on nifti files (Colorectal cancer) with python',
                           profile = hugo_profile)


  CTT.skills.add(Python, Matplotlib, Numpy, Nibabel)

  link_medium_ct = "https://hugobottois.medium.com/medical-images-visualization-with-python-b40c2eb085f7"
  link_github_ct = "https://github.com/hbiom/DataViz_CT_CCR"

  Portfoliolink.objects.create(portfolio=CTT, link_type="medium", link=link_medium_ct)
  Portfoliolink.objects.create(portfolio=CTT, link_type="github", link=link_github_ct)



  KLRG1 = Portfolio.objects.create(project_title = "Mucosal T cells study",
                           img="https://res.cloudinary.com/dmeefs6iu/image/upload/v1631626429/paper_xmss3y.jpg",
                           description= 'Phenotypic and transcriptomic signature of CD8 tissue resident memory T cell subsets in healthy and Crohn\'s disease patient intestinal mucosa',
                           profile = hugo_profile)

  KLRG1.skills.add(R, Bioinformatic, Bioconductor, Flow_cytometry,Cell_culture)

  link_article_klrg1 = "https://www.frontiersin.org/articles/10.3389/fimmu.2020.00896/full"
  Portfoliolink.objects.create(portfolio=KLRG1, link_type="article", link=link_article_klrg1)



  cv_generator = """
    Django application to create your own profile to share your skills, experiences and portfolio.
  """

  cv_generator_website = Portfolio.objects.create(project_title = "CV generator website",
                           img="https://res.cloudinary.com/dmeefs6iu/image/upload/v1628976213/cv_yrrdbv.png",
                           description= cv_generator,
                           profile = hugo_profile)

  cv_generator_website.skills.add(Python, Django, HTML, CSS, JavaScript, Heroku)


  link_github_cv = "https://github.com/hbiom/cv_generator"
  link_web_cv = "https://cvmyprofile.herokuapp.com/"

  Portfoliolink.objects.create(portfolio=cv_generator_website, link_type="github", link=link_github_cv)
  #Portfoliolink.objects.create(portfolio=cv_generator_website, link_type="website", link=link_web_cv)


  cursed = """
    Doodle like Ruby on rails meeting scheduling application simulation
  """

  cursed = Portfolio.objects.create(project_title = "Doodle clone",
                           img="https://res.cloudinary.com/dmeefs6iu/image/upload/v1628966143/doodles_iwjln1.png",
                           description= cursed,
                           profile = hugo_profile)

  cursed.skills.add(Ruby, ROR, HTML, CSS, JavaScript, Heroku)


  link_web_cd = "https://cursed-doodle.herokuapp.com/"
  link_github_cd = "https://github.com/hbiom/cursed_doodles"

  Portfoliolink.objects.create(portfolio=cursed, link_type="github", link=link_github_cd)
  Portfoliolink.objects.create(portfolio=cursed, link_type="website", link=link_web_cd)


  print("seeding done")


seed()

