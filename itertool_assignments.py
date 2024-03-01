#write python program to create iterators from several iterables in sequence iand display the type and element of the new iterator

from itertools import chain
def chain_func(a,b,c):
    return chain(a,b,c)

result = chain_func(
    [1,2,3],['a','s','d'],[1,2,3]
)
res = chain_func(
    (10,20,30),('a','b','c'),(True,None,False)
)
print("for List..........")    

print('Type :: ',type(result))
for i in result:
    print(i, end=' ')

print("\nfor tuple..........")    
print('Type :: ',type(res))
for i in res:
    print(i, end=' ')
        
################################################################################################################
#write program that generate the running product from iterables
from itertools import accumulate
import operator
def running_prod(lst):
    return accumulate(lst,operator.add)  

res1 = running_prod([1,2,3,4,5,6,7])  
for i in res1:
    print(i, end='|')
####################################################################################################################
from itertools import accumulate
import operator
def running_prod(tup):
    return accumulate(tup,operator.add)  

res1 = running_prod((1,2,3,4,5,6,7))  
for i in res1:
    print(i, end='|')

####################################################################################################################
# programm to construct an infinite iterator that returns evenly spaced values starting with a specified number and step
import itertools as it 
start = 100
step = 1
my_counter = it.count(start,step)
# infinite execution of number strated from 100
for i in my_counter:
    print (i)    

####################################################################################################################
# write python program to generate infinite cycle of elements
from itertools import cycle
for i in cycle(['s','h','r','i']):
    print(i)
# def cycle1(iter):
#     return cycle(iter) 
    
# res = cycle1(['a','b','c','d'])
# print(res)

####################################################################################################################
from itertools import cycle

def cycle1(iter):
    return cycle(iter) 
    
res = cycle1('python iter tools')
print(res)
for i in res:
    print(i)    
##################################################################################################################  
## program to make an iterator that drops element from the iterable as soon as an element is a positive number
import itertools as it 
def drop_while(nums):
    return it.dropwhile(lambda x : x<0,nums)
nums = [-1,-2,-3,-4,5,6,7,8,-10,9,2] 
res = drop_while(nums)
print("original List :: ", nums) 

print('droped element list :: ',list(res))
# for i in res :
#     print(i)