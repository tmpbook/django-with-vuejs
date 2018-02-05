from django.conf.urls import url
from rest_framework.authtoken import views as drf_views

urlpatterns = [
    url(r'^auth$', drf_views.obtain_auth_token, name='auth'),
]
