# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation

  
class PhotoUser(AbstractUser):
    about_user = models.TextField(verbose_name='О себе', max_length=500, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars', verbose_name='аватар', blank=True, null=True)
    
    ACTIVATE = 0
    BAN_SPAM = 1
    BAN_NOT_LAW = 2
    BAN_SELL_ACCOUNT = 3
    BAN_SWINDLER = 4
    BAN_PR = 5

    STATUS_CHOICES = (
        (ACTIVATE, 'Активен'),
        (BAN_SPAM, 'Бан (спам)'),
        (BAN_NOT_LAW, 'Бан (незаконные действия)'),
        (BAN_SELL_ACCOUNT, 'Бан (продажа аккаунта)'),
        (BAN_SWINDLER, 'Бан (мошенничество)'),
        (BAN_PR, 'Бан (реклама)'),
    )

    user_status = models.PositiveSmallIntegerField(choices = STATUS_CHOICES, default=ACTIVATE)
   
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'   


class Tag(models.Model):
    tag_name = models.CharField(db_index=True, verbose_name='Название тега', max_length=50)
    date_created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
       
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True, related_name='tag')
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey()

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Теги'
        index_together = [["object_id", "content_type"], ]


class Comment(models.Model):
    text = models.TextField(verbose_name='Текст')
    date_created = models.DateTimeField(db_index=True, verbose_name='Дата создания', auto_now_add=True)
    date_delete = models.DateTimeField(verbose_name='Дата удаления', blank=True, null=True)
    user = models.ForeignKey(to=PhotoUser, verbose_name='Пользователь', null=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey()

    def __str__(self):
        return '{0} {1}'.format(self.date_created, self.user)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        index_together = [["object_id", "content_type"], ]


class Like(models.Model):

    liked = models.IntegerField(verbose_name='Лайк', default=0)

    date_created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    date_delete = models.DateTimeField(verbose_name='Дата удаления', blank=True, null=True)

    user = models.ForeignKey(to=PhotoUser, verbose_name='Пользователь')
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey()

    def __str__(self):
        return '{0} by {1}'.format(self.liked, self.user)

    class Meta:
        index_together = [["object_id", "content_type"], ]
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'


class Mark(models.Model):
    NULL = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10

    MARK_CHOICES = (
        (NULL, '0'),
        (ONE, '1'),
        (TWO, '2'),
        (THREE, '3'),
        (FOUR, '4'),
        (FIVE, '5'),
        (SIX, '6'),
        (SEVEN, '7'),
        (EIGHT, '8'),
        (NINE, '9'),
        (TEN, '10'),
    )

    mark_composition = models.PositiveSmallIntegerField(verbose_name='Композиция', choices = MARK_CHOICES, default=NULL)
    mark_settings = models.PositiveSmallIntegerField(verbose_name='Настройки/техника исполнения', choices = MARK_CHOICES, default=NULL)
    mark_lighting = models.PositiveSmallIntegerField(verbose_name='Освещение', choices = MARK_CHOICES, default=NULL)
    mark_color = models.PositiveSmallIntegerField(verbose_name='Цвет', choices = MARK_CHOICES, default=NULL)
    mark_idea = models.PositiveSmallIntegerField(verbose_name='Идея', choices = MARK_CHOICES, default=NULL)

    date_created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    date_delete = models.DateTimeField(verbose_name='Дата удаления', blank=True, null=True)
    post = models.ForeignKey(to='Post', verbose_name='Пост')
    user = models.ForeignKey(to=PhotoUser, verbose_name='Пользователь')

    def __str__(self):
        return '{0} {1} {2} {3} {4} {5}'.format(self.user, self.mark_composition,
                                                self.mark_settings, self.mark_lighting,
                                                self.mark_color, self.mark_idea)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'


class Post(models.Model):
    text = models.TextField(verbose_name='Текст')
    photo = models.ImageField(upload_to='photo', verbose_name='фото', blank=True, null=True)
    date_created = models.DateTimeField(db_index=True, verbose_name='Дата создания', auto_now_add=True)
    date_delete = models.DateTimeField(verbose_name='Дата удаления', blank=True, null=True)
    user = models.ForeignKey(to=PhotoUser, verbose_name='Пользователь', related_name='user', null=True)

    tags = GenericRelation(Tag, related_query_name='posts')
    comments = GenericRelation(Comment, related_query_name='posts')
    likes = GenericRelation(Like, related_query_name='posts')

    def __str__(self):
        return '{0} {1}'.format(self.date_created, self.text)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Lesson(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=150)
    text = models.TextField(verbose_name='Текст')
    date_created = models.DateTimeField(db_index=True, verbose_name='Дата создания', auto_now_add=True)
    date_delete = models.DateTimeField(verbose_name='Дата удаления', blank=True, null=True)
    
    tags = GenericRelation(Tag, related_query_name='lessons')
    comments = GenericRelation(Comment, related_query_name='lessons')
    likes = GenericRelation(Like, related_query_name='lessons')

    def __str__(self):
        return '{0} {1}'.format(self.date_created, self.title)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
