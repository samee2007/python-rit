n=int(input("enter the year"))
if((n%400==0)or(n%100!=0)and (n%4==0)):
    print("Given Year is a leap Year")
else:
    print("Given Year is not a leap Year")

