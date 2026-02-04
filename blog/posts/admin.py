from django.contrib import admin
from .models import Category, Topic, Post


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    list_display = ['name']
    list_filter = ['name']


class TopicAdmin(admin.ModelAdmin):
    fields = ['name', 'category', 'created']
    readonly_fields = ['created']
    list_display = ['name', 'topic_category', 'created']
    list_filter = ['name']

    @admin.display(description='Topic (category)')
    def topic_category(self, obj):
        return f"{obj.name} ({obj.category.name})"


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'topic', 'created_by', 'created_at', 'updated_at', 'slug']
    readonly_fields = ['created_by', 'created_at', 'updated_at']
    list_display = ['title', 'short_text', 'topic', 'topic_category', 'created_by', 'created_at', 'updated_at']
    list_display_links = ['title', 'short_text']
    list_filter = ['title', 'topic', 'topic__category', 'created_by', 'created_at']
    prepopulated_fields = {"slug": ["title"]}

    @admin.display(description='Short text')
    def short_text(self, obj):
        words = f'{obj.text}'.split()
        if len(words) <= 5:
            return ' '.join(words)
        else:
            return ' '.join(words[:5]) + ' ...'

    @admin.display(description='Topic')
    def topic_category(self, obj):
        return f"{obj.topic.name} ({obj.topic.category.name})"

# Rejestracje
admin.site.register(Category, CategoryAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)