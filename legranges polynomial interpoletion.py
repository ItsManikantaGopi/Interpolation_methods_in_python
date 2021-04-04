from fractions import Fraction as Fa
from matplotlib import pyplot as pa

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
        #a=int(input("enter x %d value:-"%i))
       # b=int(input("enter y %d value:-"%i))
        x1.append(a)
        y1.append(b)
    return x1,y1,n
#r=[2,4.25,5.25,7.81,9.20,10.60]
#t=[7.2,7.1,6.0,5.0,3.5,5.0]
#n=5
def av(n,p):
    x=symbols('x')
    k=p
    j=x
    for i in range(n):
        if(i==k):
            continue
        j=j*(x-ceil(r[i]))
    j=j*t[k]
    g=x
    for i in range(n):
        if(i!=k):
            g=g*ceil((r[k]-r[i]))
    if(g==0):
        return 0
    else:
        return((j/x)/(g/x))
def gp(n):
    s=av(n,0)
    for i in range(1,n):
        s=s+(av(n,i))
    return simplify(s)
while 1:
    #r,t,n=tp()
    n=4
    r=[-1,-0.5,0,0.5,1,1.5,2]
    t=[1,0.5,0,0.5,1,1.5,2]
    print('x=',r)
    print('y=',t)
    p4=gp(n)
    q=str(p4)
    print('equation=',p4,"\n")
    x=int(input("enter the value:="))
    print(eval(q))
    
'''
def gph(q):
    xa=[]
    y=[]
    n=float(input("enter the range:-"))
    i=-n
    while(i<=n):
        xa.append(i)
        x=i
        f=eval(q)
        y.append(f)
        i=i+0.001
    pa.plot(xa,y,'b-')
gph(q)
pa.show()
'''


