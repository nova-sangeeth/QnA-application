from django.conf.urls import url
from .views import about_page

urlpatterns = [
    url(r'^about_page$', about_page, name='about_page')
]
