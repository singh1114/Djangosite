from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^product/cement/$', views.cement, name="cement"),
    url(r'^product/cement/$', views.cementicform, name="cement"),
    #url(r'^product/cement/output/$', views.output, name="output"),
    url(r'^product/cement/price/$', views.output, name="output"),
    url(r'^product/cement/cart.html/$', views.input, name="input"),
]