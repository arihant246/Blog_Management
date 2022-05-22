from django.contrib import admin
from .models import PostModel, CommentModels

# Register your models here.

admin.site.register(PostModel)
admin.site.register(CommentModels)