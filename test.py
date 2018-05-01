__author__ = "Neil"
__time__ = "2018/4/29 21:42"
import  requests
import json
# cookie ="ALF=1527596993; SCF=Au-0ncqPEUka5K9GGf6OW24CTp2jGe8nx00amFHVfbUvoiUMTabtqO-uqKyeLNsnQUGWDsgFqRT4n86o6dkRgtY.; SUB=_2A2534bwSDeRhGeRI6lEQ9irPwj-IHXVVLcRarDV6PUJbktANLUujkW1NUt0ipRM-Xw62b80ByiTjU0Nw55N4_du9; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5QIV-4QSfrqpOpFqYT3zYh5JpX5K-hUgL.FozceKepSoB01Ke2dJLoIpjLxKnLBo-L1KqLxKqL1K-LB-eLxKBLBo.L12zt; SUHB=0z1x0RPurK7M8R; SSOLoginState=1525009474; _T_WM=20c125033a2709cf808c321c6205ee2b; M_WEIBOCN_PARAMS=featurecode%3D20000320%26luicode%3D20000174%26lfid%3Dhotword"
# url="2613164393"
# data = {"project": "sina", "spider": "sinaspider4", "cookie": cookie, "url": url}
# result = requests.post("http://120.78.196.125/schedule.json", data=data)
# jobid="25a21a9a4ce811e8bf8700163e0ad926"
# data = {"project": "sina", "job": jobid}
# result = requests.post("http://120.78.196.125/cancel.json", data=data)
# result=json.loads(result.text)
# print(result)
import redis
# res={}
r = redis.Redis(host='120.78.196.125', port=6379)
r.lpush("a","a")
# fansparent = r.lpop(cookie + 'fansparent4')
# fansname=r.lpop(cookie + 'fansname4')
# fanslevel = r.lpop(cookie + 'fanslevel4')
# res["fansparent"]=fansparent.decode()
# res["fansname"]=fansname.decode()
# res["fanslevel"]=fanslevel.decode()
# r.delete(*r.keys(("*"+cookie+"*")))
# print(res)
# if  "哈哈哈":
#     print("1234")
# cookie="a"
# data={"cookie":cookie}
# print("123")
# res=requests.post("http://39.106.205.132/result2/", data=data)
# print(res.text)