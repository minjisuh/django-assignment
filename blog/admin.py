from django.contrib import admin
from .models import Post, Comment, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted')
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_date')
class CategoryAdmin(admin.ModelAdmin):
    # list_display = ('name')
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)