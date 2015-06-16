from django.views.generic import DetailView, ListView, CreateView
from travel.models import Segment, Comment
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, HttpResponseRedirect


class HomeView(ListView):
    model = Segment


class SegmentView(DetailView):
    model = Segment


class CommentCreate(CreateView):
    model = Comment
    fields = ['content', 'user']

    def get_success_url(self):
        return reverse("travel:home")

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.segment = get_object_or_404(Segment, slug=self.kwargs['slug'])
        comment.save()
        return HttpResponseRedirect(self.get_success_url())