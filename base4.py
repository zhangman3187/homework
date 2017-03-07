#-*- coding:utf-8 -*-

'''
题目：循环打印列表元素，知道15个

2017/3/4

'''

if __name__ == '__main__':

	count = 0
	n =0
	list = ['A','B','C','D','E','F']

	while(n < (15/len(list))+1):
		for k in list:
			if count == 15:
				break
			else:
				print k
				count+=1
		n+=1
