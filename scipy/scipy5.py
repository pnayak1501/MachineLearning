import scipy as sp
import numpy as np
from scipy import linalg

arr1 = np.array([[1,3],[2,4]])
arr2 = np.array([[5,9],[6,8]])

fun1 = sp.linalg.solve(arr1,arr2)
print(fun1)

fun2 = sp.linalg.inv(arr1)
print(fun2)
