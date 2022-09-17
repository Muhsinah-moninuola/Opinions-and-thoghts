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
from rest_framework import routers, permissions
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view


schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='1.0.0',
        description="API documentation of App",
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.Home),
    #path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/blogapp/<int:pk>/', Blogupdate.as_view()),
    path('api/blogapp/',PostAPIView.as_view()),
    path('api/auth/userlogin',LoginApiview.as_view()),
    path('api/blogapp/Blogcategory/',BlogPostCategory.as_view()),
    path('api/blogapp/Blogcategory/<int:pk>/',PostCategory.as_view()),
    path('api/auth/register/', UserRegistrationAPIView.as_view()),
    path('api/delete/<int:pk>/', DeleteAPIView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger-ui"),
    path('api/blogapp/userposts/<str:user_username>/',UserpostsApiView.as_view()),

 ]
urlpatterns += router.urls