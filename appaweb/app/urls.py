from django.conf.urls import url
from django.urls import include
from . import views
from django.contrib.auth import views as auth_views
app_name='appaweb'

urlpatterns=[
    url(r'^$', views.base, name='base'),
    url(r'^about$', views.about, name='aboutUS'),
    url(r'^package$', views.onlinePackage, name='onlinePackage'),
    url(r'^onLearn$', views.onlineLearn, name='onlineLearn'),
    url(r'^order$', views.order, name='Order'),
    url(r'^(?P<id>[0-9]{1,16})/(?P<title>[ 1-9a-zA-zآ-ی،. ?!؟ ]{1,50})/$', views.searchposts_result, name='searchposts_result'),
    url(r'^send/(?P<id>[0-9]{1,16})/(?P<title>[ 1-9a-zA-zآ-ی،؟. ?!]{1,50})/$', views.sendCm, name='sendCm'),
    url(r'^pack/(?P<id>[0-9]{1,16})$', views.packageSell, name='packageSell'),
    url(r'^learn/(?P<id>[0-9]{1,16})$', views.learnSell, name='learnSell'),
#register
    url(r'^login$', views.Login, name='Login'),
    url(r'^logout$', views.signout, name='logout'),
    url(r'^Register$', views.signup, name='Signup'),
    url(r'^reset-password/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    url(r'^reset-password/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset-password/complete/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
#zarinpal
    url(r'^request/(?P<id>[0-9]{1,16})/(?P<title>[ آ-ی]{1,50})/$', views.send_request, name='request'),
    url(r'^verify/', views.verify, name='verify'),
    url(r'^requestt/(?P<id>[0-9]{1,16})/(?P<title>[ آ-ی]{1,50})/(?P<price>[0-9]{1,16})/$', views.send_request2, name='request2'),
    url(r'^verifyy/', views.verify2, name='verify2'),
url(r'^searchblog/$',views.searchposts, name='searchposts'),
url(r'^search/$',views.searchposts_check, name='searchposts_check'),
url(r'^codeRahgiri/(?P<id>[0-9]{1,16})/$',views.rahgiri, name='rahgiri'),
    ]
