from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=256)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

class BugReport(models.Model):
	username = models.CharField(max_length=256)
	email = models.EmailField()
	bug_title = models.CharField(max_length=256)
	bug_description = models.TextField()

	def __str__(self):
		return "Bug : " + self.bug_title

class AboutMe(models.Model):
	title = 'About_me'
	first_name = models.CharField(max_length=256)
	last_name = models.CharField(max_length = 256)
	profile = models.ImageField(default='default.jpg', upload_to='About_Profile')
	description = models.TextField()
	contact = models.CharField(max_length=256)

	def __str__(self):
		return self.title


