import pandas as pd

Employee = {'number':[1,2,3,4,5],'name':['AB','Virat','Finchy','Ali','Maxwell'],'Hourly salary':[15,25,3,523,10]}
table1 = pd.DataFrame(Employee)

print(table1.head(3))
print(table1.head(1))
print(table1.tail(3))
