#!/usr/bin/python3
#简单的字典
#存储字典的列表。存储列表的字典。存储字典的字典。
#字典是一系列键值对，每个键都与一个值关联，可以使用键来访问与之相关联的值。
#alien_0={'color':'green','points':'5'}
#print(alien_0['color'])
#print(alien_0['points'])
#new_points = alien_0['points']
#print("you just earned "+str(new_points)+" "+"points")
#
#
###python不关心键值对的添加顺序，而只关心键和值之间的关联关系。
#alien_0['x_position']=0
#alien_0['y_position']=256
#print(alien_0)
#
#创建一个空字典
#alien_0={}
#alien_0['x_position']=0
#alien_0['y_position']=256
##alien_0['speed']=0
##alien_0['speed']=input("please input alien speed,you can input slow,medium.fast:  ")
#
##调试
#alien_0['speed']="slow"
#
#print(alien_0)
#if alien_0['speed'] == 'slow':
#    x_increment = 1
#elif alien_0['speed'] == 'medium':
#    x_increment = 2
#else:
#    x_increment = 3
#alien_0['x_position'] = alien_0['x_position'] + x_increment
#print("外星人的新位置为"+str(alien_0['x_position'])+"\n"+str(alien_0['y_position']))
#
#创建字典,用以下的方式创建字典 逗号
########################################################################################################
favorite_languages = {
    'tian':'100',
    'qiang':'200',
    'zhang':'300',
    'li':'400',
}

#print("tian favorite language is "+favorite_languages['tian'].title()+"!")
########################################################################################################
#
#遍历字典中的所有键
#for name in favorite_languages.keys():
#    #print(str(name.title())+"'s favorite language is "+str(language.title()))
#    print(str(name.title()))
#
#for name,language in favorite_languages.items():
#print(str(name.title())+"'s favorite language is "+str(language.title()))
    #print(str(name.title()))
for key in sorted(favorite_languages.keys()):
    print(key)    