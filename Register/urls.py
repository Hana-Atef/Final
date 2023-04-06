"""Register URL Configuration

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
from project import views
from django.contrib.auth import views as auth_views
from project.views import CustomLoginView  
from project.forms import LoginForm
from django.urls import path, include
from django.urls import re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.homepage, name="homepage"),
    path("register", views.register_request, name="register"),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='login.html',
                                    authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),


    # path("login", views.login_request, name="login"),
    # path("logout", views.logout_request, name= "logout"),


]

