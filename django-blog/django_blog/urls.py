"""django_blog URL Configuration

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
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from blog.views import iletisim, deneme, deneme_ajax, deneme_ajax_2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('blog.urls')),
    path('auths/', include('auths.urls')),
    path('following/', include('following.urls')),
    path('iletisim/', iletisim, name='iletisim'),
    path('deneme/', deneme, name='deneme'),
    path('deneme-ajax/', deneme_ajax, name='deneme-ajax'),
    path('deneme-ajax-2/', deneme_ajax_2, name='deneme-ajax-2'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
