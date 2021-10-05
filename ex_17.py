'''program is Incomplete'''

def first_differ(s1, s2):
    if s1==s2:
        return -1
    else:
        for i in s1:
            for j in s2:
                if s1.index(i)==s2.index(j):
                    if i!=j:
                        ind = s1.index(i)
                        return ind+1

print(first_differ(input(), input()))
