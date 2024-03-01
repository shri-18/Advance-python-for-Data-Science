from itertools import permutations
players = [1,2,3] #['shri','chetan','mahesh','pranav']


for i in permutations(players,2):
    print(i)