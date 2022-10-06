#!/usr/bin/python3
#切片的概念，
players = ['tian1','tian2','tian3','tian4']
#print(players[1:3])

#for player in players[:3]:
#    print(player.title())

my_players=players[:]
my_players.append('tian5')
my_players.insert(4,'tian6')
#print(my_players)
print(my_players)