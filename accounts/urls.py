from django.conf.urls import url
from .views import login_view

urlpatterns = [
    url( r'^$', login_view , name="login"),
]