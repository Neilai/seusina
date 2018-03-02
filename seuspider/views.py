from django.shortcuts import render
from django.views.generic import View
from  seuspider.models import *
from django.http import HttpResponseRedirect,HttpResponse
import json,redis
from django.core.urlresolvers import reverse
# Create your views here.

import requests

class sina(View):

    def get(self,request):
        return  render(request,"personalweibo.html")

    def post(self,request):
        cookie = request.POST.get("cookie", "")
        url = request.POST.get("url", "")
        data = {"project": "sina", "spider": "sinaspider", "cookie": cookie, "url": url}
        # result = requests.post("http://localhost:6800/schedule.json", data=data)
        return render(request, "result_sina.html", {'cookie': cookie})


class result(View):
    def post(self,request):
        res={}
        r = redis.Redis(host='127.0.0.1', port=6379)

        cookie = request.POST.get("cookie","")
        print(cookie)
        timeVal=r.lpop(cookie+'datetime')
        likenum=r.lpop(cookie+'likenum')
        repeatnum = r.lpop(cookie + 'repeatnum')
        commentnum = r.lpop(cookie + 'commentnum')

        res["time"]=(int(timeVal))
        res["likenum"]=(int(likenum))
        res["repeatnum"]=(int(repeatnum))
        res["commentnum"]=(int(commentnum))

        print(res)
        return HttpResponse(json.dumps(res), content_type='application/json')

class sina1(View):
    def get(self,request):
        return  render(request,"singleweibo.html")
    def post(self,request):

        cookie = request.POST.get("cookie", "")
        url = request.POST.get("url", "")
        data = {"project": "sina", "spider": "sinaspider2", "cookie": cookie, "url": url}
        result = requests.post("http://localhost:6800/schedule.json", data=data)
        return render(request, "result_sina1.html", {'cookie': cookie})


class result1(View):
    def post(self,request):
        res={"time":[]}
        r = redis.Redis(host='127.0.0.1', port=6379)
        cookie = request.POST.get("cookie","")
        timeVal=r.lpop(cookie+'datetime2')
        res["time"].append(int(timeVal))
        return HttpResponse(json.dumps(res), content_type='application/json')

class sina2(View):

    def get(self,request):
        return  render(request,"fans.html")
    def post(self,request):
        cookie=request.POST.get("cookie","")
        url=request.POST.get("url","")
        data = {"project": "sina", "spider": "sinaspider2", "cookie": cookie, "url": url}
        # result = requests.post("http://localhost:6800/schedule.json", data=data)
        return render(request, "result_sina2.html", {'cookie': cookie})


class result2(View):
    def post(self,request):
        res={"time":[]}
        r = redis.Redis(host='127.0.0.1', port=6379)
        cookie = request.POST.get("cookie", "")
        timeVal=r.lpop(cookie+'datetime2')
        res["time"]=int(timeVal)
        return HttpResponse(json.dumps(res), content_type='application/json')


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
