from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.generic import (
							ListView,
							DetailView,
							CreateView,
							UpdateView,
							DeleteView,
)
from . models import Post, AboutMe
from . forms import BugReportForm
# Create your views here.


def about(request):


	data = {
		'user': AboutMe.objects.filter(id=1).first(),	
		'title': "About",
	}
	return render(request, 'blog/about.html', context=data)

def announcements(request):


	data = {
			
		'title': "Announcements",
	}
	return render(request, 'blog/announcements.html', context=data)


def bug_report(request):
	if request.method == 'POST':
		form = BugReportForm(request.POST)

		if form.is_valid():
			form.save()
			messages.success(request, f'Your report has been submitted!')
			return redirect('blog-home')
	else:	
		form = BugReportForm()
	data = {
		'form': form,
		'title': "Bug Report",
	}
	return render(request, 'blog/bug_report.html', context=data)
# Using Class Based Views

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5

class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts_list.html'
	context_object_name = 'posts'
	# ordering = ['-date_posted']
	paginate_by = 5 

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')


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


# def about(request):
# 	data = {
# 		'title': 'About',
# 	}
# 	return render(request, 'blog/about.html', context=data)	