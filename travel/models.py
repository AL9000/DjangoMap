from django.db import models
from django.utils.text import slugify
import itertools


class Milestone(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


class Segment(models.Model):
    start_milestone = models.ForeignKey(Milestone, related_name="start")
    end_milestone = models.ForeignKey(Milestone, related_name="end")
    end_date = models.DateTimeField()
    pub_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    photo = models.ImageField(upload_to='photos/', )

    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def __str__(self):
        return self.end_milestone.name

    def save(self, *args, **kwargs):
        self.slug = orig = slugify(self.start_milestone.name + '-vers-' + self.end_milestone.name)
        for x in itertools.count(1):
            if not Segment.objects.filter(slug=self.slug).exists():
                break
            self.slug = '%s-%d' % (orig, x)
        super(Segment, self).save(*args, **kwargs)
