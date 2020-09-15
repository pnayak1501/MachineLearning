import numpy as np

var1 = np.array([[2,4,6],[1,3,5]])
var1 = var1.reshape(3,2)
print(var1.itemsize)
print(var1.dtype)
print(var1)