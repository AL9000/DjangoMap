from django.db import models
from django.utils.text import slugify
from django_markdown.models import MarkdownField
import itertools
from geopy.geocoders import GoogleV3


class Milestone(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField(blank=True,
                                 help_text="Latitude and longitude fields will be "
                                           "filled up automatically from city name above")
    longitude = models.FloatField(blank=True)
    arrival_date = models.DateTimeField()
    text = MarkdownField()

    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.slug = orig = slugify(self.name)
        for x in itertools.count(1):
            if not Milestone.objects.filter(slug=self.slug).exists():
                break
            self.slug = '%s-%d' % (orig, x)
        geolocator = GoogleV3()
        location = geolocator.geocode(self.name)
        self.latitude = location.latitude
        self.longitude = location.longitude
        super(Milestone, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.CharField(max_length=25)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    milestone = models.ForeignKey(Milestone, related_name='comments')


class Photo(models.Model):
    photo = models.ImageField(upload_to='photos/', )
    milestone = models.ForeignKey(Milestone, related_name='photos')

    def __str__(self):
        return self.milestone.name