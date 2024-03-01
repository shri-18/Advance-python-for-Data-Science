# Shallow copy

l = [1,2,3,4]
n = l
l[0] = -10

print(l)
print(n)
###################################################################################3
# deep copy 
# # copy() function use
# shallo copy creates 1 level deep copy.
# modifying on level 1doesnt affect the other list
# in order to create the  copy copy function of copy module is used

l = [1,2,3,4]
l1 = l.copy()
l[0] = -10
print(l)
print(l1)


###################################################################################3
import copy
a = [1,2,3,4]
b = copy.copy(a)
b[0] = -10

print(a)
print(b)
###################################################################################3
# drawback of shallo copy
import copy
a = [[1,2,3,4,5],[6,7,8,9,10]]
b= copy.copy(a)

a[0][0] = -10
print(a)                                   #[[-10, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
print(b)                                   #[[-10, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

# for two deeper level the shallo copy shows the change in both the list
# in shallow copy for nested onjects modifying on level 2 or deeper does affect the other 
###################################################################################3
