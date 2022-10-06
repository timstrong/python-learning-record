#!/usr/bin/python3
#列表适合存储在程序运行期间可能产生变化的数据集。
#python将不能修改的值成为不可变的，而不可变的列表被称为元组。使用圆括号来标识。
foods = ('apple','banana','watermelon','panapple','milk')
for food in foods:
    print(food)
foods = ('orange','banana','watermelon','panapple','water')
for food in foods:
    print(food)



