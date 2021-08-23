word=input('enter the word: ')
status = False
for i in word:
    if i in "aeiouAEIOU":
        status = True
if status == True:
    print('word contains vowels')
else: 
    print('word does not contains vowels')

    
    
    
 #Output1:
#enter the word: why
#word does not contains vowels


#Output2:
#enter the word: python
#word contains vowels
