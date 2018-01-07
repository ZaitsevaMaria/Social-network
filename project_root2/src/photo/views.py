# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from photo.models import Post, PhotoUser, Mark
from photo.models import Comment, Like, Tag, Lesson
from photo.forms import PostForm, CommentForm, SearchUserFormByUsername
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.db.models import Count
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import json
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.contrib import auth



# http://127.0.0.1:8000/photo/about/
@login_required
def about_project(request):
    return render(request, 'photo/about_project.html', {})


# http://127.0.0.1:8000/photo/posts/list/
@login_required
def posts_list(request):
    posts = Post.objects.all().select_related().annotate(num_likes=Count('likes')).order_by('-date_created') [:20]
    posts = posts.annotate(num_comments=Count('comments'))
    return render(request, 'photo/posts_list.html', {'posts': posts})


# http://127.0.0.1:8000/posts/list/user/
@login_required
def posts_list_user(request):
    posts = Post.objects.filter(user_id=request.user.id).annotate(num_likes=Count('likes')).order_by('-date_created')
    posts = posts.annotate(num_comments=Count('comments'))

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('http://127.0.0.1:8000/photo/posts/list/user/')
    else:
        form = PostForm()

    return render(request, 'photo/posts_list_user.html', {'posts': posts, 'form': form})


# http://127.0.0.1:8000/post/detail/65
def post_detail(request, post_id):

    post = get_object_or_404(Post, pk=post_id)

    marks = Mark.objects.filter(post=post)

    marks_rounded = {}
    mark_composition = marks.aggregate(avg_comp = Avg('mark_composition'))
    if mark_composition['avg_comp'] != None:
        marks_rounded['Композиция'] = round(mark_composition['avg_comp'], 2)
    else:
        marks_rounded['Композиция'] = 'нет оценок'

    mark_settings = marks.aggregate(avg_set = Avg('mark_settings'))
    if mark_settings['avg_set'] != None:
        marks_rounded['Настройки/техника исполнения'] = round(mark_settings['avg_set'], 2)
    else:
        marks_rounded['Настройки/техника исполнения'] = 'нет оценок'

    mark_lighting = marks.aggregate(avg_light = Avg('mark_lighting'))
    if mark_lighting['avg_light'] != None:
        marks_rounded['Освещение'] = round(mark_lighting['avg_light'], 2)
    else:
        marks_rounded['Освещение'] = 'нет оценок'

    mark_color = marks.aggregate(avg_color = Avg('mark_color'))
    if mark_color['avg_color'] != None:
        marks_rounded['Цвет'] = round(mark_color['avg_color'], 2)
    else:
        marks_rounded['Цвет'] = 'нет оценок'

    mark_idea = marks.aggregate(avg_idea = Avg('mark_idea'))
    if mark_idea['avg_idea'] != None:
        marks_rounded['Идея'] = round(mark_idea['avg_idea'], 2)
    else:
        marks_rounded['Идея'] = 'нет оценок'

    likes = Like.objects.select_related('user').filter(object_id=post_id)

    comments = Comment.objects.select_related('user').filter(object_id=post_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.object_id = post_id
            comment.content_type_id = 12
            comment.save()
            return redirect('http://127.0.0.1:8000/photo/post/detail/%d/' % post.id)
    else:
        form = CommentForm()

    return render(request, 'photo/post_detail.html',
                  {'post': post, 'comments': comments, 'likes': likes,
                   'marks_rounded': marks_rounded, 'form': form})


def comment_edit(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    post = get_object_or_404(Post, comments=comment_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.object_id = post.id
            comment.content_type_id = 12
            comment.save()
            return redirect('http://127.0.0.1:8000/photo/post/detail/%d/' % post.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'photo/comment_edit.html', {'comment': comment, 'form': form})


# http://127.0.0.1:8000/photo/authors_post_likes/2/
def authors_post_likes (request, post_id):
    likes = Like.objects.select_related().filter(object_id=post_id)
    return render(request, 'photo/authors_post_likes.html', {'likes': likes})


# http://127.0.0.1:8000/photo/users/list/
@login_required
def users_list(request):
    users = PhotoUser.objects.filter(user_status=0).defer('password',
                                        'last_login', 'is_superuser', 'first_name', 'last_name', 'email',
                                        'is_active', 'is_staff', 'date_joined', 'avatar')[:20]
    return render(request, 'photo/users_list.html', {'users': users})


# http://127.0.0.1:8000/photo/user/detail/2/
@login_required
def user_detail(request, user_id):
    user = get_object_or_404(PhotoUser, pk=user_id)
    posts = Post.objects.filter(user=user).annotate(num_likes=Count('likes')).order_by('-date_created')  #[:20]
    return render(request, 'photo/user_detail.html', {'user': user, 'posts': posts})


# http://127.0.0.1:8000/photo/user?username=Антон
@login_required
def users_by_name(request):
    username=request.GET['username']
    usernames = PhotoUser.objects.filter(user_status=0, username__icontains=username).defer('password',
                                        'last_login', 'is_superuser', 'first_name', 'last_name', 'email',
                                        'is_active', 'is_staff', 'date_joined', 'about_user', 'avatar')
    return render(request, 'photo/users_by_name.html', {'usernames': usernames})


# http://127.0.0.1:8000/photo/lessons/list/
@login_required
def lessons_list(request):
    lessons_list = Lesson.objects.all()
    paginator = Paginator(lessons_list, 20)
    page = request.GET.get('page')
    try:
        lessons = paginator.page(page)
    except PageNotAnInteger:
        lessons = paginator.page(1)
    except EmptyPage:
        lessons = paginator.page(paginator.num_pages)

    return render(request, 'photo/lessons_list.html', {'lessons': lessons})


# http://127.0.0.1:8000/photo/lesson/detail/2/
@login_required
def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, 'photo/lesson_detail.html', {'lesson': lesson})


# http://127.0.0.1:8000/photo/post?tag_name=Landscape
@login_required
def posts_by_tag(request):
    tag_name = request.GET['tag_name']
    posts = Post.objects.select_related().defer('user__last_login','user__password',
     'user__last_login', 'user__is_superuser', 'user__about_user', 'user__user_status',
     'user__first_name', 'user__last_name', 'user__email', 'user__is_active', 'user__is_staff',
     'user__date_joined', 'user__avatar').filter(tags__tag_name=tag_name)
    return render(request, 'photo/posts_by_tag.html', {'tag_name': tag_name, 'posts': posts})


# http://127.0.0.1:8000/photo/lesson?tag_name=Landscape
@login_required
def lessons_by_tag(request):
    tag_name=request.GET['tag_name']
    lessons = Lesson.objects.filter(tags__tag_name=tag_name)
    return render(request, 'photo/lessons_by_tag.html', {'tag_name': tag_name, 'lessons': lessons})


# @login_required
def simple_example(request):
    if request.method == "GET":
        return render(request, 'photo/simple_example.html')
    if request.method == "POST":
        data = '1'
        context = {"data": data}
        return HttpResponse(json.dumps(context), content_type="application/json")


# http://127.0.0.1:8000/photo/posts/list/user/
@login_required
def posts_list_user(request):
    posts = Post.objects.filter(user_id=request.user.id).annotate(num_likes=Count('likes')).order_by('-date_created')
    posts = posts.annotate(num_comments=Count('comments'))

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('http://127.0.0.1:8000/photo/posts/list/user/')
    else:
        form = PostForm()

    return render(request, 'photo/posts_list_user.html', {'posts': posts, 'form': form})


def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES or None, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('http://127.0.0.1:8000/photo/posts/list/user/')
    else:
        form = PostForm(instance=post)
    return render(request, 'photo/post_edit.html', {'post': post, 'form': form})


def search_user_username(request):
    if request.method == "GET":
        form = SearchUserFormByUsername()
        params = dict()
        params["search"] = form
        return render(request, 'photo/form_search_user_username.html', params)

    if request.method == "POST":
        form = SearchUserFormByUsername(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            users = PhotoUser.objects.filter(username__icontains=query)
            context = {"query": query, "users": users}
            return_str = render_to_string('part_views/_form_search_user_username.html', context)
            return HttpResponse(json.dumps(return_str), content_type="application/json")
        else:
            HttpResponseRedirect("/form_search_user_username")


# http://127.0.0.1:8000/photo/posts/list/user/
@login_required
def user_main_page(request):
    user = request.user
    return render(request, 'photo/user_main_page.html', {'user': user})


@login_required
def logout(request):
    auth.logout(request)
    return redirect('http://127.0.0.1:8000/login/')