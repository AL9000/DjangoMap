from django.conf.urls import url
from travel.views import HomeView, CommentCreate
from travel.feeds import LatestEntriesFeed

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^milestone/(?P<slug>[-\S]+)/commenter$', CommentCreate.as_view(), name='milestone_comment'),
    url(r'^latest/feed/$', LatestEntriesFeed()),
]
