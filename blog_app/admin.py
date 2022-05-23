from django.contrib import admin
from .models import PostModel, CommentModels, SubCommentModels, ContactFormModel

# Register your models here.

admin.site.register(PostModel)
admin.site.register(CommentModels)
admin.site.register(SubCommentModels)
admin.site.register(ContactFormModel)