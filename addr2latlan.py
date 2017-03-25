# -*- coding: utf-8 -*-
import urllib
import json
import urllib.request
print("请输入你想要查询的地点")
s = input()
s = urllib.parse.quote(s)
url = "http://restapi.amap.com/v3/geocode/geo?address=%s&output=JSON&key=cd1e03dcaa91a4cfd7e643a98d93a778"%(s)
req = urllib.request.urlopen(url)

data = req.read().decode('utf-8')
jsonData = json.loads(data)
#print(jsonData)
print("您所查询的地点的经度为：",float(jsonData['geocodes'][0]['location'].split(',',1)[0]))
print("您所查询的地点的纬度为：",float(jsonData['geocodes'][0]['location'].split(',',1)[1]))
s = input()
