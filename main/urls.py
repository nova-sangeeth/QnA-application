from django.conf.urls import url
from .views import index, listing, home_feed, test_view


urlpatterns = [
    url(r"^index$", index, name="index"),
    # url(r'^$', , name='')
    url(r"^test$", test_view, name="test_view"),
    url(r"^home_feed$", home_feed, name="home_feed"),
]
