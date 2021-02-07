from rest_framework import serializers
from todo_list import models
from comment import models

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ['Todo_id','title','description','is_completed','created_at','updated_at']
        model = models.Todo

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ['Comment_id','content','created_at','updated_at']
        model = models.Comment