l = [int(i) for i in input().split()]
result=[]
for i in l:
    if i not in result:
        result.append(i)
print(result)
