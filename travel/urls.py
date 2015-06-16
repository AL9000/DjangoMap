from django.conf.urls import url
from travel.views import HomeView, SegmentView, CommentCreate

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^etape/(?P<slug>[-\S]+)/$', SegmentView.as_view(), name='segment_detail'),
    url(r'^etape/(?P<slug>[-\S]+)/commenter$', CommentCreate.as_view(), name='segment_comment'),
]
