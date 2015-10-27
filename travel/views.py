from django.views.generic import ListView, CreateView
from travel.models import Milestone, Comment
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, HttpResponseRedirect


class HomeView(ListView):
    model = Milestone
    ordering = '-arrival_date'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['completed_objects'] = Milestone.completed_objects.all().order_by('-arrival_date')
        return context


class CommentCreate(CreateView):
    model = Comment
    fields = ['alias', 'content', 'photo']

    def get_success_url(self):
        return reverse("travel:home")

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.milestone = get_object_or_404(Milestone, slug=self.kwargs['slug'])
        if comment.photo:
            if comment.photo.size > 1*1024*1024:
                raise ValidationError("Réduit la taille de ton image stp ! J'ai pas les moyens d'héberger de grosses images :o")
        comment.save()
        return HttpResponseRedirect(self.get_success_url())