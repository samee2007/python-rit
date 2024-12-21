n=eval(input("enter a number")) 
org=n 
sum=0 
for i in range (n): 
    a=n%10 
    sum=sum+a*a*a 
    n=n//10
if(sum==org): 
    print("The given number is Armstrong number") 
else: 
    print("The given number is not Armstrong number") 