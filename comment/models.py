from django.db import models

class Comment(models.Model):
    Comment_id = models.AutoField(primary_key=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now = True)