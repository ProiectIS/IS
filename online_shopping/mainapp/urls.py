from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^$',views.first_page,name='first_page'),
    url(r'^main/',views.first_page,name='first_page'),
    # /shirt/id
    url(r'^shirts/(?P<shirt_id>[0-9]+)/$', views.shirt_detail, name='shirt_detail'),
    url(r'^shirts/',views.shirts_page,name='shirts_page'),
    url(r'^dresses/(?P<dress_id>[0-9]+)/$', views.dress_detail, name='dress_detail'),
    url(r'^dresses/',views.dresses_page,name='dresses_page')
]
