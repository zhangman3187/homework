#-*- coding:utf-8 -*-

import requests

if __name__ == '__main__':

	r = requests.get(url='http://www.itwhy.org')
	print r.status_code


	#带参数的get请求
	r = requests.get(url='http://dict.baidu.com/s',params={'wd':'python'})
	print r.url
	#打印解码后的返回数据
	print r.content