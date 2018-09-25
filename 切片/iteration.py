# -*- coding: utf-8 -*-


from collections import Iterable


# 如果定一个list或tuple 我们可以通过for循环了来遍历这个list或tuple 
# python通过 for...in来完成遍历

# dict的迭代
dict = {'a':1 , 'b':3 , 'c':10}

for key in dict:
	print key


# 因为dict的初春不是按照list的方式来排序 所以 迭代的顺序可能不一样，
# 默认情况下，dict迭代的是key，如果要迭代value，可以这样做
for value in dict.values():
	print value

# 同时迭代value key
for di in dict.items():
	print di

# 迭代字符串
for ch in 'ABCDEFG':
	print ch

# 在我们使用for循环，只要作用于一个可迭代对象，for循环就正常运行，而我们不太关心其数据类型
# 判断数据类型方法是否可迭代
print isinstance('abc',Iterable)
print isinstance(123,Iterable)

# 如果要对list实现类似java那样的下标循环，python 的内置enumerate函数可以吧list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：

for i , value  in enumerate(['A','V','B']):
	print i , value

# 求最大值最小值
def FindMaxAndMin(List):
	if List != []:
		max = List[0]
		min = List[0]
		for L in List:
			if max < L:
				max = L
			if min > L:
				min = L
		return (min , max)
	else: 
		return(NONE,NONE)

print FindMaxAndMin([10,30,5,1,99,55])
