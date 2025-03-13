"""
URL configuration for prj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='main/homepage.html'), name='home'),
    path('alba/', TemplateView.as_view(template_name='main/alba.html'), name='alba'),
    path('skladby/', TemplateView.as_view(template_name='main/skladby.html'), name='skladby'),
    path('kapely/', TemplateView.as_view(template_name='main/kapely.html'), name='kapely'),
    path('osobnosti/', TemplateView.as_view(template_name='main/osobnosti.html'), name='osobnosti'),
]
