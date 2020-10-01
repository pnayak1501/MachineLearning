import matplotlib.pyplot as plt

numbers = [2,3,3,42,5,53,54,455,43,243,23,4324,343,3,43,4,34,3,4,3,4,34,32,3,43,4,343,]
jumps = [0,15,30,45,60,75,90,105]

plt.hist(numbers,jumps,histtype='bar')
plt.show()
