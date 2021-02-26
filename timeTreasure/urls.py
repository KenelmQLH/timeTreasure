"""timeTreasure URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from app import views

urlpatterns = [
    path(r'',views.login),
    path(r'admin/', admin.site.urls),
    path(r'login/', views.login),

    path(r'index/<int:uid>/', views.index_projects),
    path(r'add_project/', views.add_project),
    path(r'deleteproject/', views.deleteproject),

    path(r'index_subprojects/<int:uid>/<int:pid>/', views.index_subprojects),
    path(r'add_subproject/', views.add_subproject),
    path(r'del_subproject/', views.del_subproject),
    path(r'add_record/', views.add_record),


]
