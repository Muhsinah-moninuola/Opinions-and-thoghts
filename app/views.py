from unicodedata import category
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from app.models import *
from app.serializers import *
from django.contrib.auth.hashers import make_password

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

class BlogPostCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

class PostCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    
class PostAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.filter(approval=True)
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]  

class DeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserRegistrationAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        data = serializer.validated_data
        serializer.save(password = make_password(data['password']))

class LoginApiview(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserpostsApiView(generics.ListAPIView):
    serializer_class = BlogSerializer
    permission_classes = [permissions.AllowAny]
    def  get_queryset(self):
        return Post.objects.filter(user__username = self.kwargs["user_username"], approval = True)

