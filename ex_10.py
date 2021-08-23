import random
a=[]
for i in range(20):
    a.append(random.randint(1,100))
print('list is: ',a)
print('largest element in list: ',max(a))
print('smallest element in list: ',min(a))
