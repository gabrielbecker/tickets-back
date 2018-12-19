"""blueticket URL Configuration

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
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from blueticket import settings

URL_ROOT = ''
SWAGGER_ROOT = '/' + URL_ROOT

schema_view = get_swagger_view(title='Tickets API')


def ep(regex, view, kwargs=None, name=None):
    return url(regex=r'^{}{}'.format(URL_ROOT, regex), view=view, kwargs=kwargs, name=name)


router = routers.DefaultRouter()

urlpatterns = [
    ep('', include(router.urls)),
    ep('admin/', admin.site.urls),
    ep('docs/', schema_view),
    # ep('rest-auth/', include('rest_auth.urls')),
    ep('', include('tickets.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
