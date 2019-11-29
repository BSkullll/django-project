from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import Profile


class UserRegisterForm(UserCreationForm, forms.Form):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		username = self.cleaned_data.get('username')

		if email and User.objects.filter(email=email).exclude(username=username).exists():
			raise forms.ValidationError(u'This email already exists.')
		return email	

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username','email',]

	def clean_email(self):
		email = self.cleaned_data.get('email')
		username = self.cleaned_data.get('username')

		if email and User.objects.filter(email=email).exclude(username=username).exists():
			if len(User.objects.filter(email=email).exclude(username=username))>1:
				raise forms.ValidationError(u'This email already exists.')
			return email
		return email	
	
	def clean_username(self):
		
		username = self.cleaned_data.get('username')

		if username and User.objects.filter(username=username).exists():
			if len(User.objects.filter(username=username))>1:
				raise forms.ValidationError(u'This username already exists.')
			else:
				return username	
		return username		

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']		