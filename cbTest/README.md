
Project developed using Django and djangorestframework, see requirements.txt to more info

Based on 
# Heroku Django Starter Template

https://github.com/heroku/heroku-django-template


## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate

Currently running at https://immense-bastion-59983.herokuapp.com/api/

Database used is postgreSQL, info must be setted on cbTest/settings.py