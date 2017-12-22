#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from models import *

# Create your views here.

def index(request):
    # return HttpResponse('<h1>hello world!!</h1>')
    content={'title':'首页','list':BoolInfo.objects.all()}
    return render(request,'bookdemo/index.html',content)

def detail(request,id):
    return render(request,'bookdemo/detail.html',{'book':BoolInfo.objects.get(id=id)})