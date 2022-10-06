#!/bin/bash/python3


with open('Y:\\1-learning-record\python\chapter10\\file.txt') as file_object:
    lines =  file_object.readlines()
    for line in lines:
        print(line)