from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import math

def safe_arange(start, stop, step):
  return step * np.arange(start / step, stop / step)

# domain values
x = safe_arange(-1., 1., 0.2)

# function which generates Pn(x) summation
def ntaylor_exp(n, a):
  polynomials = []
  for j in range(n + 1):
    s = [ round( ((i-a)**j)*round(math.exp(a), 3)/(math.factorial(j)), n+1 ) for i in x]
    polynomials.append(s)
  
  temp = []
  for poly in polynomials:
    if poly == polynomials[0]:
      temp = poly
      continue
    else:
      s = []
      for i, j in zip(poly, temp):
        s.append(i+j)
        
      temp = s
    
  return temp


# range values for f(x), pn(x)
fx = [round(math.exp(i), 5) for i in x] 
p1 = ntaylor_exp(1, 0)
p2 = ntaylor_exp(2, 0)
p3 = ntaylor_exp(3, 0)

# Taylor Remainder values.
r1 = [round(i - j, 2) for i, j in zip(fx, p1)]
r2 = [round(i - j, 3)  for i, j in zip(fx, p2)]
r3 = [round(i - j, 4) for i, j in zip(fx, p3)]

# grab subplots
fig, ax = plt.subplots()

# hide the axes
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

# create data
df = pd.DataFrame({
    'x': x,
    'R1(x)': r1,
    'R2(x)': r2,
    'R3(x)': r3,
    'f(x)=exp(x)': fx
})

# create table from dataframe
table = ax.table(cellText=df.values, colLabels=df.columns, loc='center')

#display table
plt.title('Taylor Approx of ln(x) on interval [1/2, 3/2]')

plt.savefig('rmndr_e_x_table.png')

plt.show()

""" 
# used to display the graph using matplotlib

# fix aspect ratios
ax.set_aspect('equal')
ax.grid(True, which='both')

ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

# graph f(x) and 1st-3rd deg taylor poly
ax.plot(x, fx, 'k', label='f(x)')
ax.plot(x, r1, 'r.', label='R1(x)')
ax.plot(x, r2, 'g.', label='R2(x)')
ax.plot(x, r3, 'b.', label='R3(x)')

ax.plot(x, p1, 'r--', label='P1(x)')
ax.plot(x, p2, 'b--', label='P2(x)')
ax.plot(x, p3, 'g--', label='P3(x)')

# legend uses label values
ax.legend()

plt.savefig("e_px_rx_graph")

plt.show()
"""