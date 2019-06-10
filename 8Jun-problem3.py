adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
l1=[]
l2=[]

print('Numbers greater than 5 are :')
for i in adhoc:
        if(i>5):
           print(i)
           l1.append(i)
print('Numbers less than or equal to 2 are :')           
for i in adhoc:
        if(i<=2):
           print(i)
           l2.append(i)

print('List of numbers greater than 5 are :')
print(l1)
print('List of numbers less than or equal to 2 are :')
print(l2)
