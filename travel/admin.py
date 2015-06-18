from django.contrib import admin
from django.db.models import TextField
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from travel.models import Milestone, Photo, Comment


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 3


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'get_arrival_date', 'get_photo']

    def get_arrival_date(self, obj):
        return obj.milestone.arrival_date
    get_arrival_date.short_description = 'arrival date'

    def get_photo(self, obj):
        return '<img src="%s" style="width:125px;"/>' % obj.photo.url
    get_photo.short_description = 'thumbnail'
    get_photo.allow_tags = True


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'content', 'get_milestone', 'pub_date', ]
    ordering = ['-pub_date', ]

    def get_milestone(self, obj):
        return obj.milestone
    get_milestone.short_description = 'milestone'


class MilestoneAdmin(MarkdownModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [PhotoInline, ]
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}
    list_display = ['name', 'arrival_date', 'display_text', 'get_photo', ]
    search_fields = ['name', 'text']
    date_hierarchy = 'arrival_date'
    ordering = ['-arrival_date', ]

    def display_text(self, obj):
        if len(obj.text) > 40:
            return obj.text[0:40] + '...'
        return obj.text
    display_text.short_description = 'text overview'

    def get_photo(self, obj):
        return '<img src="%s" style="width:125px;"/>' % obj.photos  # TODO Don't know why this
        # (with obj.photos.first.url) doesn't work
    get_photo.short_description = 'thumbnail'
    get_photo.allow_tags = True


admin.site.register(Milestone, MilestoneAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Comment, CommentAdmin)