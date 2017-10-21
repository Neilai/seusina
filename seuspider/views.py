from django.shortcuts import render
from django.views.generic import View
from  seuspider.models import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.

import requests

class sina(View):

    def get(self,request):
        return  render(request,"personalweibo.html")
    def post(self,request):
        cookie=request.POST.get("cookie","")
        url=request.POST.get("url","")
        cookie_url="COOKIE_URL="+cookie+'|'+url
        data = {"project": "sina", "spider": "sinaspider", "setting": cookie_url}
        response = requests.post("http://localhost:6800/schedule.json", data=data)
        return HttpResponseRedirect(reverse('result') )

class result(View):
    def get(self,request):
        result = Sina.objects.all()
        return render(request, "result_sina.html", {'result': result})

class sina1(View):

    def get(self,request):
        return  render(request,"singleweibo.html")
    def post(self,request):
        cookie=request.POST.get("cookie","")
        url=request.POST.get("url","")
        cookie_url="COOKIE_URL="+cookie+'|'+url
        data = {"project": "sina", "spider": "sinaspider1", "setting": cookie_url}
        requests.post("http://localhost:6800/schedule.json", data=data)
        data = {"project": "sina", "spider": "sinaspider2", "setting": cookie_url}
        requests.post("http://localhost:6800/schedule.json", data=data)
        return HttpResponseRedirect(reverse('result1'))

class result1(View):
    def get(self,request):
        commentresult = Sina1.objects.all()
        repeatresult = Sina2.objects.all()
        return render(request, "result_sina1.html", {'commentresult': commentresult, 'repeatresult': repeatresult})


class sina2(View):

    def get(self,request):
        return  render(request,"fans.html")
    def post(self,request):
        cookie=request.POST.get("cookie","")
        url=request.POST.get("url","")
        cookie_url="COOKIE_URL="+cookie+'|'+url
        data = {"project": "sina", "spider": "sinaspider3", "setting": cookie_url}
        response = requests.post("http://localhost:6800/schedule.json", data=data)

        return HttpResponseRedirect(reverse('result2'))


class result2(View):
    def get(self,request):
        result = Sina3.objects.all()
        return render(request, "result_sina2.html", {'result': result})

class sina3(View):

    def get(self,request):
        return  render(request,"socialmap.html")
    def post(self,request):
        cookie=request.POST.get("cookie","")
        url=request.POST.get("url","")
        cookie_url="COOKIE_URL="+cookie+'|'+url
        data = {"project": "sina", "spider": "sinaspider4", "setting": cookie_url}
        response = requests.post("http://localhost:6800/schedule.json", data=data)
        return HttpResponseRedirect(reverse('result3'))


class result3(View):
    def get(self,request):
        result = Sina4.objects.all()
        return render(request, "result_sina3.html", {'result': result})
