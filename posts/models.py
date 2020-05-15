from django.db import models
# models describe charateristics of the data in the database
# Create your models here.
class Post(models.Model):
    text = models.TextField()

    # displays the first 50 char of text as the object name
    def __str__(self):
        return self.text[:50]
# runs python manage.py makemigrations posts
# python manage.py migrate to activate the changes made to the database
