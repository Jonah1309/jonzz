"""master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path,include
from django.contrib import admin
from django.conf.urls.static import static
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name="main"

urlpatterns = [
	path('',views.homepage,name="homepage"),    
	url(r'^main/home.html',views.check,name="check"),
    
    url(r'^homepage_choose',csrf_exempt(views.homepage_choose),name="homepage_choose"),
    url(r'^generate_output',views.generate_output,name="generate_output"),
    url(r'^generate_new_output',views.generate_new_output,name="generate_new_output"),

]