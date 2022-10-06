#!/usr/bin/python3
##
#alien_0 = {'color':'red','point':5 } 
#print(alien_0['color'])
#print(alien_0['point'])
#print(alien_0)
#del alien_0['color']
#print(alien_0)
#
#favorite_languages = {'jen':'python','sarah':'c','edward':'ruby','phil':'python'}
#
#

#嵌套，列表，字典

#from xml.sax.handler import property_interning_dict


alien_0 = {'color':'green','points':'5'}
alien_1 = {'color':'yellow','points':'10'}
alien_2 = {'color':'red','points':'15'}

aliens=[alien_0,alien_1,alien_2]


for alien  in aliens:
    print(alien)

#随机生成外星人
aliens = []
for alien_number in range(100):
    new_alien = {'color':'green','points':'5'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)

