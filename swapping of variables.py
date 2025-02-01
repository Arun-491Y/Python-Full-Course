a=5
b=6
print('a=',a,'b=',b)#before swapping 
temp=a #now the value of a is assigned to temporary(temp) varibale.then the variable a is empty now
a=b #the value of a is assigned from the value of b 
b= temp #the value of b is assigned from the value of temp variable 
print('a=',a,'b=',b)

'Method 2'
a,b = b,a
print(a,b)

#testing 
a=5
b=10
a+=b
b=a-b
a-=b 
print(a,b)