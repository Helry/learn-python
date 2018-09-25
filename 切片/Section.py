# -*- coding: utf-8 -*- 

# 场景:取一个list或者tuple的部分元素
#
Li = ['Michael' , 'Sarah' , 'Tracy' , 'Bob' , 'Jack']
# 取前三个元素，笨方法:
print Li[0] , Li[1] , Li[2]
# 因为取前N个元素就没法取了
# 取前N个元素，也就是索引为0-（N-1)的元素，可以用循环:

last = []
n = 4

for i in range(n):
	last.append(Li[i])


print last

# 但是对于经常取指定索引范围的操作，用循环也是十分费劲，但是，python提供了切片操作符(Slice)，简化了过程
# 对于取前三个元素，使用切片一行代码搞定
print Li[0:3]
# [0:3]含义:从索引0开始取，知道索引3位置，但是不包括索引3，也就是0，1，2，正好三个元素，
# 如果第一个索引是0 还可以简写成
print Li[:3]
# 类似的就是，既然python支持list[-1]取倒数第一个元素，那么它也支持倒数切片，
print Li[-2:]

# 创建一个0-99的数列
L = list(range(100))
print L

# 取前10个数
print L[:10]
# 取后10个数
print L[-10:]
# 取11-20的输
print L[10:20]
# 前10个数，每两个取一个
print L[:10:2]
# 所有数 每5个取一个
print L[::5]

# tuple也是一种list，唯一的区别就是tuple不可变，因此，tuple也可以用切片操作，只是操作的结果仍是tuple
print (0,1,2,3,4)[:3]
# 字符串‘xxx'也可以看成是一个list，每个元素就是一个字符，因此，字符串也可以用切片操作，只是操作结果仍是字符串
print 'ABCDEFG'[:3]
print 'ABCDEFG'[::2]



# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(n):
	return n[1:len(n) - 1]


print trim(' hello world ')


