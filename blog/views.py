from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Post

# Create your views here.
def hello(request):
   #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
   return render(request, 'post_list.html')

