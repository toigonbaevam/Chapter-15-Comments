from django.contrib import admin
from .models import Article, Comment 

class CommentInline(admin.StackedInline):
    model = Comment
    
class CommentInline(admin.TabularInline):
    model = Comment
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
        ]
class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0 
admin.site.register(Article, ArticleAdmin) 
admin.site.register(Comment)
