n=int(input("enter a number")) 
sum=0
for i in range(n):
    a=n%10 
    sum=sum*10+a
    n=n//10
    if n==0:
        break
print(sum) 