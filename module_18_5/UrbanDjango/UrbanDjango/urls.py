"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from task2.views import index_func, index_class
from task4.views import  game_platform, game, cart
from task5.views import  sign_up_by_html, sign_up_by_django




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', game_platform),  # Запись для функции в файле views.py
    path('class/', index_class.as_view()),
    path('platform/', game_platform),
    path('platform/games/', game),
    path("platform/cart/", cart),
    path('platform/sing/', sign_up_by_html),
    path("platform/django/", sign_up_by_django)
]
