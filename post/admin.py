from django.contrib import admin
from post.models import Post

class postAdmin(admin.ModelAdmin):

    list_display = ['title', 'slug']
    search_fields = ['title', 'content']
    # prepopulated_fields = {'slug': ('title',)}
    class Meta:
        model = Post


admin.site.register(Post, postAdmin)