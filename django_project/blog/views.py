from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
	{
		'author': 'Gaurav Kumar',
		'title': 'Blog Post 1',
		'content': 'First post contetnt',
		'date_posted': 'August 28 2019'
	},
	{
		'author': 'Saurav Kumar',
		'title': 'Blog Post 2 ',
		'content': 'Second post content',
		'date_posted': 'August 29 2019'
	}	
]


def home(request):
	data = {
		'posts':posts,
		'title': "Home",
	}
	return render(request, 'blog/home.html', context=data)

def about(request):
	data = {
		'title': 'About',
	}
	return render(request, 'blog/about.html', context=data)	