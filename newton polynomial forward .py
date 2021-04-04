from matplotlib import pyplot as pa
from math import *
from fractions import Fraction as fa

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
    xy=xy[0]
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
    #xy,xd=tp()
    xy=[0,2,4,6,8,10,12,14,16,18,20]
    xd=[0,16,29,40,46,51,32,18,8,3,0]
    h,y=fn(xy,xd)
    l2=p(xy,h)
    d=simplify(poly(h,y,l2))
    print(d)
'''    while 1:
        x=float(input("enter the x value to evaluate:-"))
        print(eval(str(d)))
'''  
        

