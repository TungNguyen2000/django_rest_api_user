"""
URL configuration for UserModel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from UserModel import views

urlpatterns = [
    

    path('/', views.FindAll), # ..../user/
    path('/create', view.Create)
    path('/<string:id>', views.FindOne) #.../user/id
    path('/update/<string:id>', views.Update) #.../user/id
    path('/delete/<string:id>', views.Delete) #.../user/id
]
