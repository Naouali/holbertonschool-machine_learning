#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3
x = list(range(0,11))
plt.plot(x, y, 'red')
plt.xlim(0,10)
plt.show()
