# -*- coding: utf-8 -*-
from photo.views import about_project, authors_post_likes, comment_edit, lesson_detail, \
    lessons_list, post_detail,  post_edit, posts_list, posts_list_user, search_user_username, \
    simple_example, user_detail, user_main_page, users_list, logout \

from django.conf.urls import url



urlpatterns = [
    url(r'^about/$', about_project, name='about_project'),
    url(r'authors_post_likes/(?P<post_id>\d+)/$', authors_post_likes, name='authors_post_likes'),
    url(r'comment/edit/(?P<comment_id>\d+)/$', comment_edit, name='comment_edit'),
    url(r'form_search_user_username/$', search_user_username, name='search_user_username'),
    url(r'^lessons/list/$', lessons_list, name='lessons_list'),
    url(r'lesson/detail/(?P<lesson_id>\d+)/$', lesson_detail, name='lesson_detail'),
    url(r'post/edit/(?P<post_id>\d+)/$', post_edit, name='post_edit'),
    url(r'post/detail/(?P<post_id>\d+)/$', post_detail, name='post_detail'),
    url(r'^posts/list/$', posts_list, name='posts_list'),
    url(r'^posts/list/user/$', posts_list_user, name='posts_list_user'),
    url(r'^simple_example/$', simple_example, name='simple_example'),
    url(r'user_main_page/$', user_main_page, name='user_main_page'),
    url(r'^users/list/$', users_list, name='users_list'),
    url(r'user/detail/(?P<user_id>\d+)/$', user_detail, name='user_detail'),
    url(r'^logout/$', logout, name='logout'),
]

