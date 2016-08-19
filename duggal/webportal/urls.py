from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^product/cement/$', views.cementicform, name="cement"),
    #url(r'^product/cement/price/$', views.output, name="output"),
    #url(r'^product/cement/cart.html/$', views.input, name="input"),

    #urls for course aggregate
    #url(r'^product/course/$', views.courseform, name = "course"),
    #url(r'^product/course/price/$', views.courseprice, name="courseprice"),
    #url(r'^product/course/cart.html/$', views.inputcourse, name="input"),
    #url(r'^(?P<p_id>[a-z]+)/$', views.bekaar, name = "bekaar")






    # I will use this section to recreate the way urls are specified.
    # I will not change the back content.
    url(r'^product/(?P<product_name>[a-z]+)/$', views.product, name = "product"),
    url(r'^product/(?P<product_name>[a-z]+)/price/$', views.price, name = "price"),
    url(r'^cart/$', views.cart, name = "cart"),
]