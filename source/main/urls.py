"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from webapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='main_url'),
    path('details/<int:pk>', details_page, name='details_url'),
    path('create/', product_create, name='product_create_url'),
    path('edit/<int:pk>', product_edit, name='product_edit_url'),
    path('delete/<int:pk>', product_delete, name='product_delete_url'),
    path('product/<str:slug>/', cat_list, name='cat_url')
]
