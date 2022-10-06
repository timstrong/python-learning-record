#!/usr/bin/python3
#切片的概念，
players = ['tian1','tian2','tian3','tian4','tian5']
my_players=players[:]
your_players=players[:]
my_players.append('tian_append')
your_players.insert(0,'tian_insert')
print(my_players)
print(your_players)

for player in players:
    print(player)