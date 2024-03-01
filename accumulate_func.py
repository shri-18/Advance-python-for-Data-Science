#accumulate tae 2 arguments that is accumulate(iterables,function)
from itertools import accumulate
import operator
def running_prod(lst):
    return accumulate(lst,operator.add) 
    # return accumulate(lst,operator.sub)  
    # return accumulate(lst,operator.mul) 
     

res1 = running_prod([1,2,4,5,6,7])  
for i in res1:
    print(i, end=' ')
    