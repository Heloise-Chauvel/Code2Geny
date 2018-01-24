"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from . import view
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #/classe/[xxx]/
    url(r'^classe/([0-9]+)/$',view.detailsClasse,name='detailsClasse'),
    #create/[xxx]/classe/[xxx]
    url(r'^create/([0-9]+)/classe/([0-9]+)/$',view.detailsClasse2,name='detailsClasse'),
    #/devoir/[xxx]/
    url(r'^devoir/([0-9]+)/$',view.detailsDevoir,name='detailsDevoir'),
    #/devoir/creerDevoir/([0-9]+)
    url(r'^devoir/creerDevoir/([0-9]+)/$',view.remplirNouveauDevoir,name='creerDevoir'),
    #login
    path('', auth_views.login, name='login'),
    #form devoir prof   create/[xxx]
    url(r'^create/([0-9]+)/$', view.devoir_create,name="createDevoir"),
    #index
    path('index/', view.index),
    #admin
    path('admin/', admin.site.urls),
    #invoice
    url(r'^invoice/$', view.invoiceView, name='invoice'),
path('cours', view.cours),
    #login?
    url('login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)
