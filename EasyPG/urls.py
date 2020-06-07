"""EasyPG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url 
from main import views
from EasyPG import settings
from EasyPG.settings import MEDIA_ROOT,MEDIA_URL
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'logout',views.logout,name='logout'),
    url(r'display_tenant',views.display_tenant,name='display_tenant'),
    url(r'display_owner',views.display_owner,name='display_owner'),
    url(r'tenant_help',views.tenant_help,name='tenant_help'),
    url(r'owner_help',views.owner_help,name='owner_help'),
    url(r'index',views.index,name='index'),
    url(r'about',views.about,name='about'),
    url(r'signups',views.signup,name='signups'),
    url(r'signupown',views.signupown,name='signupown'),
    url(r'logins',views.login,name='logins'),
    url(r'help',views.helps,name='help'),
    url(r'termsandconditions',views.tandc,name='termsandconditions'),
    url(r'signview',views.signview,name='signview'),
    url(r'loginown',views.loginown,name='loginown'),
    url(r'loginview',views.loginview,name='loginview'),
    url(r'edit',views.edit,name='edit'),
    url(r'',views.home,name=''),
   
    
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
