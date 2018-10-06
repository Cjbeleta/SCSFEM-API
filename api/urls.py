from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^api/$', views.superadmin_list),
    url(r'^api/(?P<pk>[0-9]+)/$', views.superadmin_detail),
]