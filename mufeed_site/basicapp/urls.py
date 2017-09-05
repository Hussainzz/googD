from django.conf.urls import url
from . import views

app_name='basicapp'
urlpatterns = [

            url(r'^$', views.CourseListView.as_view(), name='list'),
            url(r'^(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name='detail'),
            url(r'^create/$', views.CourseCreateView.as_view(), name='create'),
            url(r'^update/(?P<pk>\d+)/$', views.CourseUpdateView.as_view(), name='update'),
            url(r'^delete/(?P<pk>\d+)/$', views.CourseDeleteView.as_view(), name='delete'),

    url(r'^createStudent/$', views.StudentCreateView.as_view(), name='createStudent'),
    url(r'^updateStudent/(?P<pk>\d+)/$', views.StudentUpdateView.as_view(), name='updateStudent'),
]
