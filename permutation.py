# #it gives all the possible combination 
# from itertools import permutations
# players = [1,2,3] #['shri','chetan','mahesh','pranav']


# for i in permutations(players,2):
#     print(sum(i))

from itertools import permutations
t = int(input())
x = 0
def list1(n):
    l = []
    for i in range(n+1):
        l.append(i)
    return l
for i in range(t):
    n, s = input().split()
    l = list1(int(n))
    print(l)
    for j in permutations(l,2):
        # print(j)
        if sum(j) == int(s):
            x += 1
            print(j)
    print(x)    