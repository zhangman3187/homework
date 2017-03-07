# -*- coding:utf-8 -*-

import requests,json

url='http://android.kuchuan.com/ranklatest?packagename=com.tencent.mm&market=360&date=1487690224850'
r=requests.get(url).json()
print r
print type(r)
print r[u'msg']