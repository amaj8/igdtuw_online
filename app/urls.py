from django.conf.urls import url
from . import views

app_name = 'app'
urlpatterns=[
    url(r'^$',views.HomeView.as_view(),name='home'),
    url(r'^login$',views.login_view.as_view(),name='login'),
]