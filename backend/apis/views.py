from django.shortcuts import render
from rest_framework import generics

from .serializers import TodoSerializer
from todos.models import Todo
# Create your views here.

class TodoListView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
class TodoDetailView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer