from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^city_name/$', views.CityView.as_view(), name="city_name"),
]