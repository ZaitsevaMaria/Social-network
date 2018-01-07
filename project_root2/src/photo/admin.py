# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from photo.models import PhotoUser, Post, Mark, Lesson, Tag, Comment, Like

from django.contrib.contenttypes.models import ContentType


SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'email']

class MyUserAdmin(UserAdmin):
    model = PhotoUser

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('about_user', 'avatar', 'user_status')}),
    )

class PostAdmin(admin.ModelAdmin):
    list_select_related = ('user',)
    raw_id_fields = ('user',)

class CommentAdmin(admin.ModelAdmin):
    list_select_related = ('user',)
    raw_id_fields = ('user',)

class LikeAdmin(admin.ModelAdmin):
    list_select_related = ('user',)
    raw_id_fields = ('user',)

class MarkAdmin(admin.ModelAdmin):
    list_select_related = ('user', 'post')
    raw_id_fields = ('user', 'post')


admin.site.register(PhotoUser, MyUserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Mark, MarkAdmin)
admin.site.register(Lesson)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(ContentType)
