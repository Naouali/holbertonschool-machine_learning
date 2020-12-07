#!/usr/bin/env python3
"""
change scale
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 28651, 5730)
r = np.log(0.5)
t = 5730
y = np.exp((r / t) * x)
plt.plot(x, y)
plt.yscale("log")
plt.xlim(0,)
plt.show()
