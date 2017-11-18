from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^index/$',views.index,name='index'),
    url(r'^index/$',views.IndexView.as_view(), name='index'),
    url(r'^about/$',views.about,name='about'),
    url(r'^full_width/$', views.FullWidthView.as_view() ,name='full_width'),
    url(r'^contact/$',views.contact,name='contact'),
    # url(r'^detail/post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^detail/post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    # url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
]
