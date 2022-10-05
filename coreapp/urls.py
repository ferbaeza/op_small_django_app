"""coreapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static 

from login import views


urlpatterns = [
    path('', views.login, name="login"),
    path('admin/', admin.site.urls, name="admin"),
    path('home/', include('home.urls')),
    path('library/', include('library.urls')),
    path('appStore/', include('appStore.urls')),
    path('register/', include('register.urls')),
    path('login/', include('login.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('blog/', include('blog.urls')),
    path('generator/', include('generator.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#]+static(settings.STATIC_URL, document_root=settings.STATIC_FILES_DIRS)
