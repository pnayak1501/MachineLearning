import numpy as np

var1 = np.array([[2,4,6],[1,3,5]])
var2 = np.array([[5,9,3],[6,7,15]])

# print(var1.ravel())
print(var1.sum(axis=0))
print(var1.sum(axis=1))

print(np.sqrt(var1))
print(np.std(var1))
