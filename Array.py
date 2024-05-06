from array import *

#int
#vals=array('i', [10,20,25,630,40,50])
#Characters

#vals= array('u', ['G', 'a','u'])
#for i in vals:
 #   print("Enter Value: " ,i)

#case 2:
#values= array('i',[10,20,25,630,40,50])
#newArray= array(values.typecode,(a*a for a in values))
#print("New Value: " ,newArray)

#case 3:

arr=array('i',[])
n =int(input("Enter the length of the array "))

for i in range(n):
    x=int(input("Enter the value of Array "))
    arr.append(x)

print(arr)

val= int(input("Enter the value for search "))
e=0
for k in (arr):
    if k==val:
        print("Value is found at index ", e)
        break

    e = e + 1


