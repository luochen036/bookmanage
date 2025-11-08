"""
URL configuration for bookmanage project.

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
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.Index.as_view(), name='index'),
    path('manage/', views.Book.as_view(), name='manage'),
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('editbook/<int:id>/', views.EditBook.as_view(), name='editbook'),
    path('addbook/', views.Addbook.as_view(), name='addbook'),
    path('deletebook/', views.Deletebook.as_view(), name='deletebook'),
    path('publish/', views.Publishmanage.as_view(), name='publish'),
    path('addpublish/', views.Addpublish.as_view(), name='addpublish'),
    path('editpublish/<int:id>/', views.Editpublish.as_view(), name='editpublish'),
    path('deletepublish/', views.Deletepublish.as_view(), name='deletepublish'),
    path('author/', views.Authormanage.as_view(), name='author'),
    path('addauthor/', views.Addauthor.as_view(), name='addauthor'),
    path('editauthor/<int:id>/', views.Editauthor.as_view(), name='editauthor'),
    path('deleteauthor/', views.Deleteauthor.as_view(), name='deleteauthor'),
]
