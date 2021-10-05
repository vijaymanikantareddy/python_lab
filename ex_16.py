def sum_digits(num):
    l = [int(i) for i in num]
    return sum(l)
a = input('enter number: ')
print(sum_digits(a))
