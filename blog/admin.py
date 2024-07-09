from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display =('title', 'content', 'slug', 'status', 'create_on')
    list_filter = ('status',)
    search_fields = ['title', 'slug']

admin.site.register(Post, PostAdmin)