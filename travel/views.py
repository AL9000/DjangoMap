from django.views.generic import DetailView, ListView
from travel.models import Segment


class HomeView(ListView):
    model = Segment


class SegmentView(DetailView):
    model = Segment