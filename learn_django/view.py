# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

from django.http import HttpResponse

# from app.models import db


def hello(request):
    context      = {}
    context['hello']='python'
    return render(request,'hello.html',context)

def index(request):
    return render_to_response('index.html')

def search_form(request):
    return render_to_response('search_form.html')
def search(request):
    request.encoding='utf-8'
    if 'q' in request.GET:
        message='你搜索的内容为：'+request.GET['q'].encode('utf-8')
    else:
        message='你提交了空表单'
    return HttpResponse(message)

def search_post(request):
    ctx={}
    ctx.update(csrf(request))
    if request.POST:
        ctx['rlt']=request.POST['q']
    return render(request,'post.html',ctx)
# def db(request):
# 	db1=db(name='w3cschool.cc')
# 	db1.save()
# 	return HttpResponse('<p>success</P>')