from matplotlib import pyplot as pa
from fractions import Fraction as fa
from math import *
from sympy import *
x=symbols('x')
def tp():
    x=symbols('x')
    n=int(input("enter no of data points:-"))
    x1=[]
    y1=[]
    for i in range(n):
        a=float(input("enter x %d value:-"%i))
        b=float(input("enter y %d value:-"%i))
        x1.append(a)
        y1.append(b)
    return x1,y1
def nfd(y):
    df=[]
    k=len(y)
    for i in range(k-1):
        po=y[i+1]-y[i]
        df.append(round(po,5))
    return(df)
def fn(a,y):
    l=[]
    sm=[]
    xy=nfd(a)
    xy=xy[len(xy)-1]
    for i in range(len(y)):
        l.append(y)
        a=nfd(y)
        y=a
    for i in range(len(l)):
        sm.append(l[i][0])
        print(l[i],"\n")
    return(xy,sm)
def p(y,h):
    l2=[]
    l2.append(1)
    p=x/x
    for i in range(len(y)):
        p=p*(x-round(y[i],5))/h
        l2.append(p)
    return(l2)
def poly(h,xy,l2):
    d=x-x
    for i in range(len(xy)):
        j=l2[i]
        d=d+((xy[i])*j)/factorial(i)
    return d
while 1:
    xy,xd=tp()
    #xy=[10,15,20,25,30,35]
    #xd=[19.27,21.51,22.47,23.52,24.65,25.89]
    h,y=fn(xy,xd)
    print(y)
    l2=p(xy,h)
    d=simplify(poly(h,y,l2))
    print(d)
    while 1:
        x=float(input("enter the x value to evaluate:-"))
        print(eval(str(d)))

        

