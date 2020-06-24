from django.conf.urls import url
from .views import about_page, search_page

urlpatterns = [
    url(r"^about_page$", about_page, name="about_page"),
    url(r"^search$", search_page, name="search_page"),
]
