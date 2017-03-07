#-*- coding:utf-8 -*-

import requests
import re


if __name__ == '__main__':

	response = requests.get('http://www.baidu.com')
	htmlData = response.content

	links = re.findall(r'a href=http://\S+',htmlData)
	print '\n'.join(links)

