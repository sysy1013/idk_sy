from rest_framework import serializers
from todo_list import models

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['Todo_id','title','description','is_completed','created_at','updated_at']
        model = models.Todo
