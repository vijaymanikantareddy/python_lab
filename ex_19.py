def is_sorted(l):
    r = sorted(l)
    if r==l:
        return True
    else:
        return False

l = [int(i) for i in input().split()]
print(is_sorted(l))
