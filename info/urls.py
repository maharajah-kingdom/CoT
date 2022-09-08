from django.urls import path
from info.views import *
from django.urls import include
from . import views
from django.contrib.staticfiles.urls import static
from django.conf import settings

urlpatterns = [
    path('', views.register),
#    path('', views.updated),
]

urlpatterns += static(settings.MEDIA_URL)