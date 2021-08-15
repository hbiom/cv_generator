
# CV website generator

![caption](https://github.com/hbiom/cv_generator/blob/main/demo_web.gif)


Django application to create your own profile to share your skills, experiences and portfolio.

**Technologies :** Django, HTML, CSS, SCSS, JS, Cloudinary, Heroku

Deploy on heroku [Here](https://cvmyprofile.herokuapp.com/profil/HugoBottois)


## Utilization


You can clone/fork the repo and add your profile through the admin page with a superuser.

Create a superuser with the command below with a name, email and a password.

```
python manage.py createsuperuser
```

You can reset your password user with this command :

```
python manage.py changepassword <user_name>
```

Then, you can add data through the admin page :


- First create your profile with your first name, last name, title, your profile type and a little text about you.

- Create your skills. Each skills can be affected by a category and a subcategory (only skills with core_skill = True will be display in skill session).

- Create your diploma, portfolio, experiences and publication (both portfolio and experience can be affected with specific skills under technical track session).

- you can add a link for your website, github repository and medium article to each portfolio project.

- Network include medium, linkdin and github profile and will be display in the website footer and in the profile presentation session under your name


## Deployment


### heroku

Your can deploy this website on heroku adding this files to your repo :

- Procfile
- requirements.txt
- runtime.txt

### Cloudinary

For upload and store image in heroku, we used cloudinary service. Create a cloudinary account and use API credential in setting.py as below :


```
cloudinary.config(
  cloud_name = str(os.getenv('CLOUD_NAME')),
  api_key = str(os.getenv('API_KEY')),
  api_secret = str(os.getenv('API_SECRET'))
)
```

You need to keep your API crendential secret using **.env** and dotenv zero-dependency module.

### URL

Your website URL will be like ```https://<site_name>.herokuapp.com/profil/<Fisrt_name><Last_name>```


## Conclusion

You can of course change design and CSS to further personalize your profile.

Thanks for reading !

Feedback are welcome and will be appreciated.



## Initial Django, React and SASS setup

The project layout for Django, SASS and React used is describe [Here](https://www.trell.se/blog/recommended-django-react-sass-project-layout/)
