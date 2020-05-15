from django.contrib import admin

#to register model 
from .models import Post
# Register your models here.
admin.site.register(Post)




# to access admin page run python manage.py createsuperuser