#!/usr/bin/python
# -*- coding: utf-8 -*-


from django.contrib import admin

# Register your models here.
from homeworkapp.models import Article, Comment,Ticket,UserProfile


admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Ticket)
admin.site.register(UserProfile)

