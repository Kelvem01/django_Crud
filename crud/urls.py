"""
URL configuration for crud project.

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
from django.urls import path, include
from inicio.views import inicio,cadastrar,listar,update,detalhes,delete

urlpatterns = [
    
    path("admin/", admin.site.urls),
    path('', inicio,name="inicio"),
    path('cadastrar/', cadastrar,name="cadastrar"), 
    path('editar/', listar,name="listar"),
    path('update/<int:id>', update,name="update"),
    path('detalhes/', detalhes,name="detalhes"),
    path('delete/<int:id>', delete,name="delete"),
    
    
]
