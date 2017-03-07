#-*- coding:utf-8 -*-

'''
题目：任意一个英文的纯文本文件，统计其中单词出现的个数

遇到问题：字典操作不熟悉

2017-3-2

'''

if __name__ == '__main__':
	
	wordList = []
	wordsDict = {}

	file = open('countWords.txt','r')
	wordsLine = file.readlines()
	#print wordsLine
	 
	#将文件内容写入list中
	for word in wordsLine:
		wordList.extend(word.strip().strip(',').split(' '))

	wordsCount = len(wordList)
	print 'countWords.txt total words is：%d\n' % wordsCount

	#判断单词在不在字典，如果存在 个数+1，否则为1
	for key in wordList:
		#if wordsDict.has_key(key):
		if key in wordsDict:
			wordsDict[key] += 1
		else:
			wordsDict[key] = 1
	print wordsDict












