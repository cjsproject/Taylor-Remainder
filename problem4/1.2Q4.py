from matplotlib import pyplot as plt
import numpy as np
import math

"""
* find linear and quadratic
* Taylor Remainder for
* sin(x) ~ x
"""

# temporary fix to floating point arithmetic error
def safe_arange(start, stop, step):
  return step * np.arange(start / step, stop / step)

# domain values
x = safe_arange(round(-math.pi/4, 4), round(math.pi/4, 4), 0.1 )

def f(n):
  return math.sin(n)

# range values f1(x)=sin(x), f2(x)=x
f1 = [round(f(i), 5) for i in x] 
f2 = [i for i in x]

# for each y value in f1, f2:
# subtract and create the range of error
err = [abs(i - j) for i, j in zip(f1, f2)]

# range values are created based on percent
#  error for sin(x), e.g. (sin(1) - 1)/sin(1) 
pcnt_err_sin = [0 if j == 0 else abs(i/j) for i, j in zip(err, f1)]

# range values are created based on percent
# error for sin(x), e.g. (sin(1) - 1)/1
pcnt_err_x = [0 if j == 0 else abs(i/j) for i, j in zip(err, f2)]

# grab subplots
fig, ax = plt.subplots(2)

# fix aspect ratios
ax[0].set_aspect('equal')
ax[0].grid(True, which='both')
ax[1].set_aspect('equal')
ax[1].grid(True, which='both')

ax[0].axhline(y=0, color='k')
ax[0].axvline(x=0, color='k')
ax[1].axhline(y=0, color='k')
ax[1].axvline(x=0, color='k')

# worst case error method,
# same as max(err)
#y = [(math.pi**3)/((4**3)*math.factorial(3)) for i in x]
y = [max(err) for i in x]


# plot the functions, errors and %err
ax[0].plot(x, f1, 'k', label='sin(x)')
ax[0].plot(x, f2, 'k.', label='y = x')
ax[1].plot(x, y, 'k', label='error bound')
ax[1].plot(x, err, 'r--', label='error')
ax[1].plot(x, pcnt_err_sin, 'g--', label='% err sin')
ax[1].plot(x, pcnt_err_x, 'b--', label='% err x')

# legend uses label values
ax[0].legend()
ax[1].legend()

plt.savefig("2gph_sin_to_x_err")

plt.show()