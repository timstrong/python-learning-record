#!/usr/bin/python3
age = int(input("please input your age : "))

if age < 4:
    price=1
elif age <=18:
    price=10
elif age <=65:
    price=20
else:
    price=100000000000
print("your cost is $"+str(price))
