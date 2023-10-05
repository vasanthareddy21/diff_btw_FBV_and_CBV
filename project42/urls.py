"""
URL configuration for project42 project.

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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('Fbv/',Fbv,name='Fbv'),
    path('Cbv/',Cbv.as_view(),name='Cbv'),

    path('Fbv_render/',Fbv_render,name='Fbv_render'),
    path('Cbv_render/',Cbv_render.as_view(),name='Cbv_render'),

    path('insert_fbv/',insert_fbv,name='insert_fbv'),
    path('Insert_Cbv/',Insert_Cbv.as_view(),name='Insert_Cbv'),

    path('CBV_Template',CBV_Template.as_view(),name='CBV_Template'),
]


