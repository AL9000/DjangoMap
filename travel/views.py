from django.views.generic import DetailView
from travel.models import Segment


class SegmentView(DetailView):
    model = Segment