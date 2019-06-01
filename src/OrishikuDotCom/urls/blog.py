"""OrishikuDotCom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib              import admin
from django.conf.urls.static     import static
from django.conf                 import settings
from django.urls                 import path, include
from django.contrib.flatpages import views as fpviews
from django.conf.urls import handler400,handler403,handler404,handler500

fpviews.DEFAULT_TEMPLATE = 'Pages/default.html'

from dapricot.blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dapricot.blog.urls', namespace='oblog'))
]
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('p/', include('dapricot.pages.urls')),
]

handler400 = 'dapricot.core.views.error_400'
handler403 = 'dapricot.core.views.error_403'
handler404 = 'dapricot.core.views.error_404'
handler500 = 'dapricot.core.views.error_500'