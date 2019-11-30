from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
							ListView,
							DetailView,
							CreateView,
							UpdateView,
							DeleteView,
)
from . models import Post
# Create your views here.



# def home(request):
# 	data = {
# 		'posts':Post.objects.all(),
# 		'title': "Home",
# 	}
# 	return render(request, 'blog/home.html', context=data)
# Using Class Based Views

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted'] 

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView( LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object() 
		if self.request.user == post.author:
			return True
		else:
			return False		

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
	model = Post	
	success_url = '/'
	def test_func(self):
		post = self.get_object() 
		if self.request.user == post.author:
			return True
		else:
			return False


def about(request):
	data = {
		'title': 'About',
	}
	return render(request, 'blog/about.html', context=data)	