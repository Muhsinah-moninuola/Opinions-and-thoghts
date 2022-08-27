from dataclasses import fields
from rest_framework import serializers
from app.models import *

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        read_only = ['created_at']
        exclude = []

class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=4)
    username = serializers.CharField(max_length=30, min_length=4)
    class Meta:
        model = User
        fields =['id', 'email', 'username', 'phone_number','age', 'gender', 'country']
