l=[]
for j in range(0,5):
    a=int(input("enter the list"))
    l.append(a) 
for i in range(1,len(l),1): 
    print(l[i:]+l[:i])  
   
     
 