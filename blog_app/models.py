from distutils.command.upload import upload
from time import time
from django.db import models
from tinymce import models as tinymce_models
from django.contrib.auth.models import User


# Create your models here.
class PostModel(models.Model):
    post_title = models.CharField(max_length=50, null=False)
    post_summary = models.TextField()
    post_body = tinymce_models.HTMLField()
    post_image = models.ImageField(upload_to='post_images/', null=True)

    def __str__(self) -> str:
        return self.post_title

class CommentModels(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    comment_body = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.comment_body
    

# class SubCommentModels(models.Model):
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
#     comment_body = models.TextField()
#     added_at = models.DateTimeField(auto_now_add=True)
#     comment = models.ForeignKey(comment_body, on_delete=models.CASCADE)

    
        
    


