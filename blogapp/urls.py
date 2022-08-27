"""blogapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.Home),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/blogapp/<int:pk>/', Blogupdate.as_view()),
    path('api/blogapp/',PostAPIView.as_view()),
    path('api/auth/register/', UserRegistrationAPIView.as_view()),
    path('api/delete/<int:pk>/', DeleteAPIView.as_view())
 ]
