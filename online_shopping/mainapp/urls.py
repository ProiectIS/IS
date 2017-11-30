from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^$',views.first_page,name='first_page'),
    url(r'^prodTable/',views.prod_table,name='prod_table'),
    url(r'^main/',views.first_page,name='first_page'),
    # /shirts/id
    url(r'^shirts/(?P<shirt_id>[0-9]+)/$', views.shirt_detail, name='shirt_detail'),
    url(r'^shirts/',views.shirts_page,name='shirts_page'),
    url(r'^dresses/(?P<dress_id>[0-9]+)/$', views.dress_detail, name='dress_detail'),
    url(r'^dresses/',views.dresses_page,name='dresses_page'),
    url(r'^sweaters/(?P<sweater_id>[0-9]+)/$', views.sweater_detail, name='sweater_detail'),
    url(r'^sweaters/',views.sweaters_page,name='sweaters_page'),
    url(r'^coats&jackets/(?P<coat_id>[0-9]+)/$', views.coat_detail, name='coat_detail'),
    url(r'^coats&jackets/',views.coats_page,name='coats_page'),
    url(r'^jeans/(?P<jean_id>[0-9]+)/$', views.jean_detail, name='jean_detail'),
    url(r'^jeans/',views.jeans_page,name='jeans_page'),
    url(r'^skirts/(?P<skirt_id>[0-9]+)/$', views.skirt_detail, name='skirt_detail'),
    url(r'^skirts/',views.skirts_page,name='skirts_page'),
    url(r'^shoes/(?P<shoe_id>[0-9]+)/$', views.shoe_detail, name='shoe_detail'),
    url(r'^shoes/',views.shoes_page,name='shoes_page')
]
