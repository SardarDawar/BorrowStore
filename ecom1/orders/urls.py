from django.conf.urls import url
from . import views

app_name = 'orders'

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    url(r'^borrow/$', views.Borrowed_items, name='Borrowed_items'),
    url(r'^(?P<id>\d+)/$', views.borrow_detail, name='borrow_detail'),
    url(r'^return/(?P<i_d>\d+)$',views.returning_items , name='return_items'),
]