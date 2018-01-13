from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout

urlpatterns = [
    url(r'^$',views.first_page,name='first_page'),
    url(r'^prodTable/',views.prod_table,name='prod_table'),
    url(r'^custTable/', views.cust_table, name='cust_table'),
    url(r'^orderTable/', views.order_table, name='order_table'),
    url(r'^main/',views.first_page,name='first_page'),
    # women
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
    url(r'^cart/',views.cart_page,name='cart_page'),
    url(r'^order/',views.order_page,name='order_page'),
    #others
    url(r'^register/',views.register,name='register'),
    url(r'^profile/(?P<id>[0-9]+)/$',views.profile,name='profile'),
    url(r'^log_in/',login,{'template_name':'log_in.html'}),
    url(r'^log_out/',logout,{'template_name':'log_out.html'}),
    url(r'^stores/', views.stores, name='stores'),
    url(r'^policies/', views.policies, name='policies'),
    url(r'^contact/', views.contact, name='contact'),
    #men
    url(r'^tshirts/(?P<tshirt_id>[0-9]+)/$', views.tshirt_detail, name='tshirt_detail'),
    url(r'^tshirts/',views.TshirtView.as_view(),name='tshirts_page'),
    url(r'^hoodies/(?P<hoodie_id>[0-9]+)/$', views.hoodie_detail, name='hoodie_detail'),
    url(r'^hoodies/', views.HoodieView.as_view(), name='hoodie_page'),
    url(r'^Mjeans/(?P<Mjean_id>[0-9]+)/$', views.Mjeans_detail, name='Mjeans_detail'),
    url(r'^Mjeans/', views.MjeansView.as_view(), name='Mjeans_page'),
    url(r'^Mjackets/(?P<Mjacket_id>[0-9]+)/$', views.Mjackets_detail, name='Mjackets_detail'),
    url(r'^Mjackets/', views.MjacketsView.as_view(), name='Mjackets_page'),
    url(r'^cart_detail/', views.cart_detail, name='cart_detail'),
    url(r'^add/(?P<product_id>[0-9]+)/$',views.cart_add, name='cart_add'),
    url(r'^update/(?P<product_id>[0-9]+)/$',views.cart_update, name='cart_update'),
    url(r'^remove/(?P<product_id>[0-9]+)/$', views.cart_remove, name='cart_remove'),
    url(r'^order_create/', views.order_create, name='order_create'),
    url(r'^place_order', views.place_order,name='place_order'),

    url(r'^(?P<product_id>[0-9]+)/$', views.product_detail, name='product_detail')
]
