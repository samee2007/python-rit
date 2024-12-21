def newtonsqrt(n): 
    root=n/2 
    for i in range(10): 
        root=(root+n/root)/2 
    print(root) 
n=eval(input("enter number to find Sqrt: ")) 
newtonsqrt(n) 