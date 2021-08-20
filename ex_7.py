a=float(input('enter number A: '))
b=float(input('enter number B: '))
if round(abs(a-b),3)<=0.001:
    print('close')
else:
    print("not close")
    
    
#Output
#enter number A: 5.001
#enter number B: 5.002
#close
