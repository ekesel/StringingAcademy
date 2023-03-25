"""stringing URL Configuration

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
from django.urls import path
from home.views import index, about, contact, pricing, privacy, terms, cancellation, shipping
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('pricing', pricing, name='pricing'),
    path('privacy',privacy,name='privacy'),
    path('terms', terms,name='terms'),
    path('cancellation', cancellation, name='cancellation'),
    path('shipping',shipping,name='shipping')
]

admin.site.site_header = "Stringing Academy"
admin.site.site_title = "Stringing | Admin"
admin.site.index_title = "Admin Eke Welcomes You"


if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  