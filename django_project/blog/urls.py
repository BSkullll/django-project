from django.conf.urls import url
from . import views 

urlpatterns = [
	url(r'^$', views.PostListView.as_view(), name='blog-home'),
	url(r'^user/(?P<username>[\w.@+-]+)/$', views.UserPostListView.as_view(), name='postss-users'),
	url(r'^post/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='post-detail'),
	url(r'^post/new/$', views.PostCreateView.as_view(), name='post-create'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post-update'),
	url(r'^post/(?P<pk>\d+)/delete/$', views.PostDeleteView.as_view(), name='post-delete'),
	url(r'^about/$', views.about, name='blog-about'),
	url(r'^announcements/$', views.announcements, name='announcements'),
	url(r'^report_bug/$', views.bug_report, name='report_bug'),


]