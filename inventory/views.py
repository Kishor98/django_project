from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone


# Create your views here.
def new_item(request):
   #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
   return render(request, 'new_item.html')