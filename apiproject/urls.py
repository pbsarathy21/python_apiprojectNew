"""apiproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from taskapp.views import TaskViewSet
from taskapp.views import Path
from taskapp.views import TaskApi
from taskapp.test import test

# router = routers.DefaultRouter()
# router.register('task', TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('test/', test),
    path('api/', TaskViewSet.as_view()),
    path('path/<int:pk>', Path.as_view()),
    path('path/', TaskApi.as_view()),
]
