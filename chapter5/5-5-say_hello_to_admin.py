#!/usr/bin/python3

names = ["admin","test1","test2","test3"]
#names = []
name_input  = input("please input your name : ")

if names:
    for name in names:
        if name == name_input:
            print("hello :"+ name)
        else:
            print("fuck")
else:
    print("list is empty")


#多重条件  多重if判断
