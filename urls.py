from django.conf.urls import url

from .views import OrderView, OrdersView
# from .views import ExampleClassBased, ExampleView, Basee, function_view

urlpatterns = [
    url(r'^order/(?P<id>\d+)', OrderView.as_view(), name='order_url'),
    url(r'^', OrdersView.as_view(), name='main'),
    # url(r'^f', function_view),
    # url(r'^c', ExampleClassBased.as_view()),
    # url(r'^e',ExampleView.as_view()),
    # url(r'^',Basee.as_view()),
]