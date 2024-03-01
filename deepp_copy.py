# full independent object were created
# deep copy
# is done by deepcopy function of copy module 
import copy
a = [[1,2,3,4,5],[6,7,8,9,10]]
b = copy.deepcopy(a)
a[0][0]= -10
print(a)                      #[[-10, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
print(b)                      #[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
####################################################################################################################









