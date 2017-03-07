#-*- coding:utf-8 -*-

'''
题目：熟悉dict的方法
dict = {"a":"apple","b":"banana","c":"grape","d":"orange"}
输出dict的value列表并进行排序

遇到问题：

2017-3-3

'''

if __name__ == '__main__':

	dict = {"a":"banana","b":"orange","c":"grape","d":"aapple"}
	list = []

	list = dict.values()
	list.sort()
    
	print list

	del(dict["a"])
	dict.pop("b")
	print dict


