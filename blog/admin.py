from django.contrib import admin
from blog.models import *

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post

    list_display = (
        "id",
        "title",
        "subtitle",
        "publish_date",
        "published",
    )
    list_filter = (
        "published",
        "publish_date",
    )
    list_editable = (
        "title",
        "subtitle",
        "publish_date",
        "published",
    )
    search_fields = (
        "title",
        "subtitle",
        "body",
    )
    date_hierarchy = "publish_date"
    save_on_top = True