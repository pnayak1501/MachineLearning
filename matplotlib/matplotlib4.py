import matplotlib.pyplot as plt

food = ['pizza','ice cream','burgers']
sales = [20,10,30]
color = ['red','blue','yellow']

plt.pie(sales,labels=food,colors=color)
plt.show()
