def number_of_factors(num):
    factors = [i for i in range(1,num+1) if num%i==0]
    print(factors)
    return len(factors)

n = int(input('enter number: '))
print(number_of_factors(n))
