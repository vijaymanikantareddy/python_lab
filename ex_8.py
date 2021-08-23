word=input('enter the word: ')
status = False
for i in word:
    if i in "aeiouAEIOU":
        status = True
if status == True:
    print('word contains vowels')
else: 
    print('word does not contains vowels')

    
s=input("enter a string: ")
v=0
for i in s:
    if i=='a' or i=='e' or i=='o' or i=='u' or i=='i' or i=='A' or i=='E' or i=='O' or i=='U' or i=='I':
        v=v+1
if v==0:
    print('string does not contains vowels')
else:
    
    print('string contains vowels.')
    
    
    
 #Output1:
#enter the word: why
#word does not contains vowels


#Output2:
#enter the word: python
#word contains vowels
