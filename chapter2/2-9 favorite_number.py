#!/usr/bin/python3
#输入一个最喜欢的值
number=int(input("please input my favorite number:\n"))
while(1==1):
    number=int(input("please reinput my favorite number:\n"))
    if number>100:
        print("number is too big\n")
    elif number<100:
        print("number is too small\n")
    else:
        print("you are right ! congratulation ! \n")
        break
