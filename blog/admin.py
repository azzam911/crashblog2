from django.contrib import admin
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    search_fields = ["title", "intro", "body"]
    list_display = ['title', 'slug','category' , 'created_at', 'status']
    list_filter = ['category', 'created_at', 'status']
    prepopulated_fields= {'slug': ('title',)}
    list_editable = ['status', 'category']

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields= {'slug': ('title',)}




admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

