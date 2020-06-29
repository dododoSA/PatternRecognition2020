import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import math

X = np.arange(-20, 20, 0.1)

PXY1 = norm.pdf(X, -1, 2) # p(x|y=1)
PXY2 = norm.pdf(X, 2, 3) # p(x|y=2)

PX = (PXY1 + PXY2)/2 # p(x)

PY1X = PXY1/PX/2 # p(y=1|x)
PY2X = PXY2/PX/2 # p(y=2|x)


plt.plot(X, PY1X, label='p(y=1|x)')
plt.plot(X, PY2X, label='p(y=2|x)', color='r')
plt.legend()
plt.show()