from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard$', views.dashboard),
    url(r'^create/(?P<user_id>\d+)$', views.create),
    url(r'^show/(?P<user_id>\d+)$', views.show),
    url(r'^remove/(?P<user_id>\d+)$', views.remove),

]