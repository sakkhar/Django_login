from django.conf.urls import url
#from login_user import views
from login_user import views
app_name = 'login_user'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^$', views.logout_user, name='logout_user'),
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username')]