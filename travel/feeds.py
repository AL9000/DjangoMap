from django.contrib.syndication.views import Feed
from travel.models import Milestone

# TODO Ca serait cool de faire une page pour chaque milestone, et la rebalancer dans le flux rss
class LatestEntriesFeed(Feed):
    title = "Niouzes from Australia"
    link = "/sitenews/"
    description = "Les derniers posts de notre périple en Australie."

    def items(self):
        return Milestone.objects.order_by('-arrival_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text