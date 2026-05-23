from math import *
f=lambda x: 1/sqrt(1+(x**2))  
x0= float(input("Enter the lower limit: "))
x1= float(input("Enter the upper limit: "))
n= int(input("Enter the number of parts: "))
h= (x1 - x0)/n
s= 0 
if n%2==0:
    for i in range (0,n+1):
        xi=x0+ i*h
        if i==0 or i==n:
            s= s+ f(xi)
        elif i%2==0:
            s = s+ 2*f(xi)
        else:
            s= s+ 4*f(xi)
    print("the value of the integral is: %.03f" %((s*h)/3))
elif n%3==0:
    for i in range (0,n+1):
        xi=x0+ i*h
        if i==0 or i==n:
            s= s+ f(xi)
        elif i%3==0:
            s = s+ 2*f(xi)
        else:
            s= s+ 3*f(xi)
    print("the value of the integral is: %.03f" %(s*h*3/8))
else:
    print("n needs to be either even or divisible by 3")
