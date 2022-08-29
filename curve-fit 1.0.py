import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
# Here is the place to put the curve you want, such as quadratic, linear, etc.
def quadratic_fit(x,a,b,c):
    return a*x**2+b*x+c
# Below is to input your data, and we choose x as absorbance; y as concentration here
x=np.array([25,125,250,500,750,1000,1500,2000])
x=np.sort(x) 
y0=np.array([2.239,1.8474,1.3456,1.0648,0.7357,0.4118,0.2267,0.0631])
y0=np.sort(y0)
guess_a=10.0
guess_b=-0.5
guess_c=2000.0
#x-y algo
par0,cov0=optimize.curve_fit(quadratic_fit,y0,x,p0=[guess_a,guess_b,guess_c]) #This is the command to perform curve fit
yf=np.linspace(0.0,np.max(y0),len(x))
xf0=quadratic_fit(yf, *par0)
#r^2 is still under construction
    #r_sq=r2_score(y0,yf)
    #print(r_sq)
a=par0[0]
b=par0[1]
c=par0[2]
# This is the print of equation of line fit
print("The line fit for BCA is:", a,"x^2+",b,"x+",c)
#test group
print("y1=", a*np.max(y0)**2+b*np.max(y0)+c,"this should be the maximum concentration of the data")
#real data
# n and t array is to input the data we obtain
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
plt.plot(yf,xf0,"b--",label="line fit for BCA")
plt.plot(y0,x,"ko", label="BCA-test")
plt.xlabel("Absorbance")
plt.ylabel("Concentration")
plt.legend()
plt.show()