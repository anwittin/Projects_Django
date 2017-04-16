from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp", "updated", "slug"]
    list_display_links = ('timestamp', 'updated')
    list_editable = ['title', 'slug']
    list_filter = ('title', 'updated')
    search_fields = ['title', 'content']
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
