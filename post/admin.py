from django.contrib import admin
from post.models import Post

class postAdmin(admin.ModelAdmin):

    list_display = ['title']
    search_fields = ['title','content']
    class Meta:
        model = Post


admin.site.register(Post, postAdmin)