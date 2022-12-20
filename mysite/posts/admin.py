from django.contrib import admin
from .models import Post, Likepost

admin.site.register(Post)
admin.site.register(Likepost)