"""django_2 URL Configuration

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
from django.urls import path, include

from apartments.views import home_view, detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apartments.api.urls')),
    # path('api/detail/<int:id>/',detail_view, include('apartments.api.urls')),
    path('', home_view, name='home-view'),
    path('detail/<int:id>/', detail_view, name='datail-view'),
    path('api-auth/', include('rest_framework.urls'))
]
