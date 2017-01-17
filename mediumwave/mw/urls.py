from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.freq_list, name="freq_list"),
]
