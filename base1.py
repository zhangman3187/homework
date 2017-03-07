# -*- coding:utf-8 -*-

#取list中最大的两个数，只用一次for循环

dataList = [23,12,45,34,8]

m1=dataList[0]
m2=dataList[1]
if m1 < m2:
    tmp = m1
    m1 = m2
    m2 = m1
for i in range(2,len(dataList)):
    if dataList[i] > m1:
        tmp = m1
        m1 = dataList[i]
        m2 = tmp
    elif dataList[i]>m2:
        m2 = dataList[i]
print m1,m2



