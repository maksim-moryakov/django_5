from django.contrib import admin
from .models import Post


# импортировали модель Post в админку
admin.site.register(Post)
