import matplotlib.pyplot as plt
from matplotlib import style

# style.use('bmh')
# style.use('classic')
style.use('dark_background')

# plt.plot([1,3,5,10],[5,10,25,125])  TODO: For one function
# plt.show()

# TODO: For more than one function
x= [2,4,6]
y= [2,4,4]

x1= [2,4,16]
y1= [2,4,20]

plt.plot(x,y)
plt.plot(x1,y1)
plt.title("TEST")
plt.xlabel('test x values')
plt.ylabel('test y values')
plt.show()

