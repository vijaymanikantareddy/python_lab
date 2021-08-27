try:
    a=int(input('enter a: '))
    b=int(input('enter b: '))
    c=a//b
except ZeroDivisionError:
    print("division is not possible with b=0")
else:
    print('a//b is',c)
finally:
    print('end of the program')
