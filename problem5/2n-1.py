from matplotlib import pyplot as plt
import numpy as np
from math import pi, sin
import math

"""
* How large should degree
* 2n-1 be chosen for error less than
* or equal to 0.001?
* f(x) = sin(x), a = pi/4 ??0??
* interval is [-pi/2, pi/2]
* and P2n-1(x) has an error of 0.001
"""

# all functions share this domain
x = np.arange(-pi/2, pi/2, 0.01)
a = 0

# f(x)= e^(cos(x))
def f(n):
  return sin(n)

# creates a list of range values for (dy/dx)^n, 
# i think this finds gradient, as in derivative at each point?
def deriv(n=1):
  return [dydx(j, degree=n) for j in x]
  
# generalized derivative: (dy/dx)^n?
def dydx(v, degree):
  h = math.exp(-6)
  if degree > 1:
    return dydx((f(v) - f(v-h))/(h), degree-1)
  else:
    return (f(v) - f(v-h))/(h)


# generalized Taylor Polynomial attempt
def nth_taylor_poly(n):
  j = pi/2
  sum_poly = 0
  for i in range(n+1):
    if i == 0:
      sum_poly += f(j)
    else:
      sum_poly += ((j - a)**i)*dydx(a, degree=i)/(math.factorial(i))
  
  return round(sum_poly, 4)


fx = [f(i) for i in x]

error = abs(f(pi/2) - nth_taylor_poly(1))
print(error)

# check remainder, infinite loop DO NOT Run
# it's 11pm and I have to be up at 7am
while error > 0.001:
  i = 0
  error = abs(f(pi/2) - nth_taylor_poly(2*i+1) )
  i += 1
  print(error)
