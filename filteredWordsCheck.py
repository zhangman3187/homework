#-*- coding:utf-8 -*-

'''
用户输入敏感词时，打印Freedom;否则打印Human Rights
敏感词文件：filtered_words.txt

遇到问题：编码格式
1：读取文件时，文件内容为utf-8
2：终端输入汉字编码要为utf-8

2017-3-1

'''


import codecs

if __name__ == '__main__':
	keywordsList=[]
	keyword = raw_input('please input the keyword: ') 
	#print keyword
    
	file = codecs.open('filtered_words.txt','r','utf-8')
	for key in file.readlines():
		keywordsList.append(key.strip())
	#print keywordsList  

	for i in range(len(keywordsList)):
		if keyword == keywordsList[i].encode('utf-8'):
			print 'Freedom'
			exit()
	print 'Human Rights'

	file.close()


