from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.first_page,name='first_page'),
    url(r'^prodTable/',views.prod_table,name='prod_table'),
    url(r'^custTable/', views.cust_table, name='cust_table'),
    url(r'^main/',views.first_page,name='first_page'),
    # /shirts/id
    url(r'^shirts/(?P<shirt_id>[0-9]+)/$', views.shirt_detail, name='shirt_detail'),
    url(r'^shirts/',views.ShirtsView.as_view(),name='shirts_page'),
    url(r'^dresses/(?P<dress_id>[0-9]+)/$', views.dress_detail, name='dress_detail'),
    url(r'^dresses/',views.DressesView.as_view(),name='dresses_page'),
    url(r'^sweaters/(?P<sweater_id>[0-9]+)/$', views.sweater_detail, name='sweater_detail'),
    url(r'^sweaters/',views.SweatersView.as_view(),name='sweaters_page'),
    url(r'^coats&jackets/(?P<coat_id>[0-9]+)/$', views.coat_detail, name='coat_detail'),
    url(r'^coats&jackets/',views.CoatsView.as_view(),name='coats_page'),
    url(r'^jeans/(?P<jean_id>[0-9]+)/$', views.jean_detail, name='jean_detail'),
    url(r'^jeans/',views.JeansView.as_view(),name='jeans_page'),
    url(r'^skirts/(?P<skirt_id>[0-9]+)/$', views.skirt_detail, name='skirt_detail'),
    url(r'^skirts/',views.SkirtsView.as_view(),name='skirts_page'),
    url(r'^shoes/(?P<shoe_id>[0-9]+)/$', views.shoe_detail, name='shoe_detail'),
    url(r'^shoes/',views.ShoesView.as_view(),name='shoes_page'),
    url(r'^cart/',views.cart_page,name='cart_page'),
    url(r'^customer_form/',views.CustomerCreate.as_view(),name='customer-add'),
    url(r'^customer_profile/(?P<pk>[0-9]+)/$',views.customer_profile,name='customer_profile'),
    url(r'^log_in/',views.log_in_page,name='log_in_page')
]
