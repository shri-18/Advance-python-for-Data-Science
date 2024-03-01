#it gives all the possibel combination bbut not reapeat
from itertools import combinations

l = [1,2,3]
for i in range(len(l)):
    for j in combinations(l,i+1):
        print(j)
        



















