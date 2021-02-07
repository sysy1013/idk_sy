from django.urls import path

from .views import ListTodo, DetailTodo , ListComment, DetailComment

urlpatterns = [
    path('',ListTodo.as_view(),ListComment.as_view()),
    path('<int:pk>/',DetailTodo.as_view(),ListComment.as_view()),
]