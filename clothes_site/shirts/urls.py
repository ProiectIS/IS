from . import views
from django.conf.urls import include,url

urlpatterns = [
    url(r'^$',views.shirtView,name='shirtView'),
    # /shirt/id
    url(r'^(?P<shirt_id>[0-9]+)/$', views.shirtDetail, name='shirtDetail')
]