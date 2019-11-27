from django.shortcuts import render
from django.http import HttpResponse
from . models import Post
# Create your views here.



def home(request):
	data = {
		'posts':Post.objects.all(),
		'title': "Home",
	}
	return render(request, 'blog/home.html', context=data)

def about(request):
	data = {
		'title': 'About',
	}
	return render(request, 'blog/about.html', context=data)	