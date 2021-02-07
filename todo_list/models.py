from django.db import models

class Todo(models.Model):
    Todo_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title