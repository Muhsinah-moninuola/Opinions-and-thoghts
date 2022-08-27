from django.shortcuts import render
from rest_framework import generics, permissions
from app.models import *
from app.serializers import *

# Create your views here.
"""
def Home(request):
    template_name = 'index.html'
    return render(request, template_name)
"""

class Blogupdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.AllowAny]

class PostAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.AllowAny]  

class DeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

class UserRegistrationAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        data = serializer.validated_data
        serializer.save(password = make_password(data['password']))



