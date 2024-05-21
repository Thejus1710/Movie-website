"""
URL configuration for movieproject1 project.

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

from django.urls import path

from . import views

urlpatterns = [
    path('registration/',views.registration,name='registration'),
    path('',views.index,name='index'),
    path('login/add/',views.add,name='add'),
    path('home/',views.home,name='home'),
    path('login/movie/<int:movie_id>/',views.detail,name='detail'),
    path('login/',views.login,name='login'),
    path('login/movie/<int:movie_id>/rating/',views.rate,name='rate')
]
