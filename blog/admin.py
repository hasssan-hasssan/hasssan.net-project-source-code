from django.contrib import admin
from blog.models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish', 'author', 'status',)
    list_filter = ('status', 'publish')
    ordering = ['status', '-publish']
    date_hierarchy = 'create'
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('body',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'create', 'active_status')
    list_filter = ('post', 'active_status', 'create', 'project')
    date_hierarchy = 'create'
    search_fields = ('body',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'create', 'link')
    ordering = ['-publish', ]
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'create'


@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('post',)


@admin.register(Teach)
class TeachesListAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_added')
    list_filter = ('date_added', )
    ordering = ['-date_added']
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Reply)

