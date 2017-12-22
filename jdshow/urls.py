from django.conf.urls import url
from.views import index,detail

urlpatterns = [
    url(r'^index/', index),
    url(r'^(?P<product_id>\d+)/$',detail,name="product"),

]