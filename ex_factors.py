def num_of_factors(num):
    factors=[i for i in range(1,num+1) if num%i==0]
    print(factors)
    return len(factors)
num=int(input('enter an integer: '))
print(num_of_factors(num)) 
