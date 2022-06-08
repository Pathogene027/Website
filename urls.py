"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from .views import about, blog1, blog2, blog3, home, login, register, single, contact

urlpatterns = [
    path('', home, name='homepage'),
    path('about/', about, name='aboutpage'),
    path('blog1/', blog1, name='blog1page'),
    path('blog2/', blog2, name='blog2page'),
    path('blog3/', blog3, name='blog3page'),
    path('contact/', contact, name='contactpage'),
    path('login/', login, name='loginpage'),
    path('register/', register, name='registerpage'),
]
