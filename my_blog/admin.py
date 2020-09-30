from django.contrib import admin
from .models import Blog, User, Comment, Genre

admin.site.register(Blog)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Genre)
