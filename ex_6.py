import random
r=random.randint(1,10)
while True:
    guess=int(input('guess the number: '))
    if r==guess:
        print('congrats! You guessed correctly')
        break
    else:
        print('Try again!')
        
        
#Output:
#guess the number: 5
#Try again!
#guess the number: 6
#Try again!
#guess the number: 6
#Try again!
#guess the number: 6
#Try again!
#guess the number: 6
#Try again!
#guess the number: 5
#Try again!
#guess the number: 7
#Try again!
#guess the number: 8
#congrats! You guessed correctly
