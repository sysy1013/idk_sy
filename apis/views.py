from rest_framework import generics
from todo_list import models
from comment import models
from .serializers import TodoSerializer, CommentSerializer

class ListTodo(generics.ListCreateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer

class ListComment(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class DetailComment(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerialize
