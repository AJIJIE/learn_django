# -*- coding: utf-8 -*-

from django.http import HttpResponse

from app.models import db

# 数据库操作
def db(request):
	db1=db(name='w3cschool.cc')
	db1.save()
	return HttpResponse('<p>success</P>')



