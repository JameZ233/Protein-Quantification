import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
def quadratic_fit(x,a,b,c):
    return a*x**2+b*x+c
x=np.array([25,125,250,500,750,1000,1500,2000])
y0=np.array([2.239,1.8474,1.3456,1.0648,0.7357,0.4118,0.2267,0.0631])
y0=np.sort(y0)
guess_a=10.0
guess_b=-0.5
guess_c=2000.0
#x-y algo
par0,cov0=optimize.curve_fit(quadratic_fit,y0,x,p0=[guess_a,guess_b,guess_c])
yf=np.linspace(0.0,np.max(y0),8)
xf0=quadratic_fit(yf, *par0)
#r_sq=r2_score(y0,yf)
#print(r_sq)
a=par0[0]
b=par0[1]
c=par0[2]
print("The line fit for BCA is:", a,"y^2+",b,"y+",c)
#test group
print("x1=", a*np.max(y0)**2+b*np.max(y0)+c)
#real data
n1=np.array([0.3232
,0.3002
,0.3264])
mean=np.mean(n1)
cx=quadratic_fit(mean,*par0)
print("concentration for normal 1 is:", cx)
n2=np.array([0.1852
,0.2159
,0.1666])
mean=np.mean(n2)
cx=quadratic_fit(mean,*par0)
print("concentration for normal 2 is:", cx)
n3=np.array([0.0939
,0.0885
,0.0878])
mean=np.mean(n3)
cx=quadratic_fit(mean,*par0)
print("concentration for normal 3 is:", cx)
n4=np.array([0.0549
,0.0421
,0.0504
])
mean=np.mean(n4)
cx=quadratic_fit(mean,*par0)
print("concentration for normal 4 is:", cx)
t1=np.array([0.2605
,0.2856
,0.2608
])
mean=np.mean(t1)
tx=quadratic_fit(mean,*par0)
print("concentration for test 1 is:", tx)
t2=np.array([0.1347
,0.126
,0.136
])
mean=np.mean(t2)
tx=quadratic_fit(mean,*par0)
print("concentration for test 2 is:", tx)
t3=np.array([0.067
,0.0723
,0.0734
])
mean=np.mean(t3)
tx=quadratic_fit(mean,*par0)
print("concentration for test 3 is:", tx)
t4=np.array([0.0389
,0.0388
,0.0365
])
mean=np.mean(t4)
tx=quadratic_fit(mean,*par0)
print("concentration for test 4 is:", tx)
#plot thing
f=plt.figure(1)
plt.plot(yf,xf0,"b--",label="line fit for BCA")
plt.plot(y0,x,"ko", label="BCA-test")
plt.xlabel("Absorbance")
plt.ylabel("Concentration")
plt.legend()
f.show()

#y-x algo
par0,cov0=optimize.curve_fit(quadratic_fit,x,y0,p0=[guess_a,guess_b,guess_c])
xf=np.linspace(0.0,np.max(x),8)
yf0=quadratic_fit(xf, *par0)
a=par0[0]
b=par0[1]
c=par0[2]
print("The line fit for BCA is:", a,"x^2+",b,"x+",c)
#test group
fitfunc=np.array([a,b,c-np.max(y0)])
concen=np.roots(fitfunc)
concen=concen[concen<3000]
print("x1=", concen)
#real data
mean=np.mean(n1)
fitfunc=np.array([a,b,c-mean])
concen=np.roots(fitfunc)
concen=concen[concen<3000]
print("concentration for normal 1 is:", concen)
mean=np.mean(n2)
fitfunc=np.array([a,b,c-mean])
concen=np.roots(fitfunc)
concen=concen[concen<3000]
print("concentration for normal 2 is:", concen)
mean=np.mean(n3)
fitfunc=np.array([a,b,c-mean])
concen=np.roots(fitfunc)
concen=concen[concen<3000]
print("concentration for normal 3 is:", concen)
mean=np.mean(n4)
fitfunc=np.array([a,b,c-mean])
concen=np.roots(fitfunc)
concen=concen[concen<3000]
print("concentration for normal 4 is:", concen)
mean=np.mean(t1)
fitfunc=np.array([a,b,c-mean])
concen=np.roots(fitfunc)
concen=concen[concen<3000]
print("concentration for test 1 is:", concen)
mean=np.mean(t2)
fitfunc=np.array([a,b,c-mean])
concen=np.roots(fitfunc)
concen=concen[concen<3000]
print("concentration for test 2 is:", concen)
mean=np.mean(t3)
fitfunc=np.array([a,b,c-mean])
concen=np.roots(fitfunc)
concen=concen[concen<3000]
print("concentration for test 3 is:", concen)
mean=np.mean(t4)
fitfunc=np.array([a,b,c-mean])
concen=np.roots(fitfunc)
concen=concen[concen<3000]
print("concentration for test 4 is:", concen)
#plot thing
g=plt.figure(2)
plt.plot(xf,yf0,"b--",label="line fit for BCA")
plt.plot(x,y0,"ko", label="BCA-test")
plt.xlabel("Concentration")
plt.ylabel("Absorbance")
plt.legend()
g.show()
input()
