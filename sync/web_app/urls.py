from django.contrib import admin
from django.conf.urls import url, include
from web_app.views import WebAppView

urlpatterns = [
    url(r"^home/$", WebAppView.as_view(), name="web_get_home"),
]
