"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.contrib.sitemaps import views
from home.views import StaticViewSitemap

sitemaps = {'static': StaticViewSitemap}

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    # path('sitemap.xml', sitemap,
    #         {'sitemaps': sitemaps}),
    path('sitemap.xml', views.index,
        {
        'sitemaps': sitemaps,
        'template_name': 'sitemap.html'
        },
        name='django.contrib.sitemaps.views.index'
    ),
     path('sitemap-<section>.xml', views.sitemap, {
        'sitemaps': sitemaps,
        'template_name': 'sitemap.html'
    }, name='django.contrib.sitemaps.views.sitemap'),
]
