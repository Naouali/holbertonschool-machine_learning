#!/usr/bin/env python3
"""
histogram
"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)
bins = [x * 10 for x in range(11)]
plt.hist(student_grades, bins=bins, align='mid', edgecolor='black')
plt.xlim(0, 100)
plt.title("Project A")
plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.show()
