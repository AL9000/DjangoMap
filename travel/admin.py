from django.contrib import admin
from django.db.models import TextField
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from travel.models import Milestone, Photo, Comment


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 3


class CommentInline(admin.TabularInline):
    model = Comment


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['milestone', 'arrival_date', 'thumbnail', ]
    search_fields = ['milestone__title', ]

    def arrival_date(self, obj):
        return obj.milestone.arrival_date
    arrival_date.short_description = "date d'arrivée"

    def thumbnail(self, obj):
        return '<a href="%s"><img src="%s" style="width:125px;"/></a>' % (obj.photo.url, obj.photo.url)
    thumbnail.allow_tags = True
    thumbnail.short_description = "miniature"


class CommentAdmin(admin.ModelAdmin):
    list_display = ['alias', 'content', 'milestone', 'pub_date', ]
    ordering = ['-pub_date', ]
    search_fields = ['alias', 'content', 'pub_date', 'milestone__title', ]


class MilestoneAdmin(MarkdownModelAdmin):
    inlines = [PhotoInline, CommentInline, ]
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}
    list_display = ['title', 'arrival_date', 'text_overview', 'lien_video', 'thumbnail', ]
    search_fields = ['title', 'text']
    date_hierarchy = 'arrival_date'
    ordering = ['-arrival_date', ]

    def lien_video(self, obj):
        if obj.video:
            return True
        return False
    lien_video.boolean = True

    def text_overview(self, obj):
        if len(obj.text) > 40:
            return obj.text[0:40] + '...'
        return obj.text
    text_overview.short_description = "aperçu du texte"

    def thumbnail(self, obj):
        return '<img src="%s" style="width:125px;"/>' % obj.photos.first  # TODO Don't know why this
        # (with obj.photos.first.url) doesn't work
    thumbnail.allow_tags = True
    thumbnail.short_description = "miniature"


admin.site.register(Milestone, MilestoneAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Comment, CommentAdmin)