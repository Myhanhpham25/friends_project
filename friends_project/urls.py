from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.login_app.urls')),
    url(r'^friends_app/', include('apps.friends_app.urls')),
]
