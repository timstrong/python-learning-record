#!/usr/bin/python3

#列表是由一系列按特定顺序排列的元素组成
#用方括号表示列表[]，逗号分隔其中的元素
from email import message


bicycles = ['trek','annondale','redline','specialized']
for bicycle in bicycles:
    print("hello my bicycle" + " " + bicycle)

#末尾添加元素
bicycles.append('hello')
#任意位置插入元素
bicycles.insert(0,'hello')
#删除元素
del bicycles[0]
#使用pop方法删除元素,删除列表末尾的元素
bicycles.pop()
#根据值删除元素
too_expensive = 'annondale'
bicycles.remove(too_expensive)
#排序
bicycles.sort()
#临时排序
print(sorted(bicycles))
#倒序
bicycles.sort(reverse=True)
for bicycle in bicycles:
    print("hello my bicycle" + " " + bicycles)