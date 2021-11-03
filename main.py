import numpy as np
def f1(x):
    return 14*x-8
def f2(x):
    return np.cos(x)
def f3(x):
    return (x-5)/(x**3+9*x**2+27*x+27)
def f4(x):
    return x/(np.sqrt(1+x**2))
x0=[1,np.pi/4,1,5]
fx1=f1(x0[0])
fx2=f2(x0[1])
fx3=f3(x0[2])
fx4=f4(x0[3])
print('f1(1)=', fx1)
print('f2(pi/4)={:.5f}' .format(fx2))
print('f3(1)=', fx3)
print('f4(5)={:.5f}'.format(fx4))
def gx(x,f,d):
    return (f(x+d)-f(x))/d
def F1(x):
    return 7*x**2-8*x+1
def F2(x):
    return np.sin(x)
def F3(x):
    return (1-x)/(x+3)**2
def F4(x):
    return np.sqrt(1+x**2)
gx1=gx(x0[0],F1,0.1)
gx2=gx(x0[1],F2,0.1)
gx3=gx(x0[2],F3,0.1)
gx4=gx(x0[3],F4,0.1)
print('tilnærming ved bruk av g(x) med f1 og x0 =1 : {:.5f}'.format(gx1))
print('tilnærming ved bruk av g(x) med f2 og x0 = pi/4 : {:.5f}'.format(gx2))
print('tilnærming ved bruk av g(x) med f3 og x0 = 1 : {:.5f}'.format(gx3))
print('tilnærming ved bruk av g(x) med f4 og x0 = 5 : {:.5f}'.format(gx4))

def Ex(f,g):    #Definerer E(x)=f'(x)-g(x)
    return np.abs(f-g)
ex1=Ex(fx1,gx1)
ex2=Ex(fx2,gx2)
ex3=Ex(fx3,gx3)
ex4=Ex(fx4,gx4)
print('E(x)=d/dx f1(x)-g(x)',ex1)
print('E(x)=d/dx f2(x)-g(x)',ex2)
print('E(x)=d/dx f3(x)-g(x)',ex3)
print('E(x)=d/dx f4(x)-g(x)',ex4)

def g(f,e):
    return np.abs(f-e)
gp1=g(fx1,0.001)
print(gp1)