from dataclasses import fields
from os import access
from rest_framework import serializers
from app.models import *
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        read_only = ['created_at']
        exclude = ['approval']
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        read_only = ['created_at']
        exclude = []

class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=4)
    username = serializers.CharField(max_length=30, min_length=4)
    class Meta:
        model = User
        fields =['id', 'email', 'username', 'password', 'phone_number','age', 'gender', 'country']

class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=30, min_length=4)
    password = serializers.CharField(max_length=10, min_length=6, write_only=True)
    tokens = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields =['id', 'username', 'password', 'tokens']

    def get_tokens(self, obj):
        user = User.objects.get(username=obj['username'])

        return{
            'refresh': user.tokens()['refresh'],
            'access' : user.tokens()['access']
            }

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed('Invalid Credentials, try again')
        return super().validate(attrs)