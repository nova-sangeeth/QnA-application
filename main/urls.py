from django.conf.urls import url
from .views import index, listing, home_feed, test_view


urlpatterns = [
    url(r'^$', index, name='index'),
    # url(r'^$', , name='')
    url(r'^test$', test_view, name='test_view'),
    url(r'^home$', home_feed, name='home_feed')
]

