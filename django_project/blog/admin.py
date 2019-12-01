from django.contrib import admin
from . models import Post, BugReport ,AboutMe
# Register your models here.


admin.site.register(Post)
admin.site.register(BugReport)
admin.site.register(AboutMe)