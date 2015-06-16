from django.forms import ModelForm
from travel.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'user']