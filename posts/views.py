from django.shortcuts import render

from django.views.generic import ListView

from .models import Post
# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    # list view returns returns the info in a variable "object_list"

    context_object_name = 'all_posts_list' # to change the name of the variable