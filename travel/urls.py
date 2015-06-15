from django.conf.urls import url
from travel.views import SegmentView

urlpatterns = [
    url(r'^etape/(?P<slug>[-\S]+)/$', SegmentView.as_view(), name='segment_detail'),
]
