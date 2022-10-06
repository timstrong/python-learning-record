#!/usr/bin/python3
#类库

class Dog():
    def __init__(self,name,age):  #特殊方法，
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title()+"is now setting")
    def roll_over(self):
        print(self.name.title()+"is now rolling")


mydog=Dog('gg','10')
print(mydog.name.title())