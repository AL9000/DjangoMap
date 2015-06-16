from django.conf.urls import url
from travel.views import HomeView, SegmentView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^etape/(?P<slug>[-\S]+)/$', SegmentView.as_view(), name='segment_detail'),
]
