
#zip function

name = ['dada','mama','kaka','babba']
info = [1234,4567,7890]

for nm , inf in zip(name,info):
    print(nm,inf)
    
################################################################################
'''This will assign the 'none' value who the element does not have any element in 2nd list to atteched '''    
from itertools import zip_longest
name = ['dada','mama','kaka','babba']
info = [1234,4567,7890]
for nm , inf in zip_longest(name,info):
    print(nm,inf)
################################################################################
'''This will assign the '0' value who the element does not have any element in 2nd list to atteched '''    
from itertools import zip_longest
name = ['dada','mama','kaka','babba']
info = [1234,4567,7890]
for nm , inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)
################################################################################
#all() function

l = [1,2,4,5,6,7]

if all(l):
    print(True)   
else :
    print(False)    
     
################################################################################
#any() function 

l = [0,0,0,0,0,7,0]    
if any(l):
    print('It has some value')
else:
    print('Useless')    

l = [0,0,0,0,0,0,0]    
if any(l):
    print('It has some value')
else:
    print('Useless')    
    
################################################################################
#Count

from itertools import count
counter = count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

#################################################################################
#cycle()
#repeat infinitely
from itertools import cycle
l = [1,2,3,4]
for i in cycle(l):
    print
    
#################################################################################
#Repeat()
from itertools import repeat

for i in repeat('keep patience',times=3):
    print(i)
        