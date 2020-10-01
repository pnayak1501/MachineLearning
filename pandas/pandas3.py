import pandas as pd

food1 = {'number':[1,2,3,4,5],'name':['corn','banana','orange','pizza','burger'],'price':[8,2,33,2,33]}
food2 = {'number':[1,2,3,4,5],'name':['apple','banana','beans','pizza','burger'],'price':[23,5,33,2,33]}

table1 = pd.DataFrame(food1)
table2 = pd.DataFrame(food2)

fusion = pd.merge(table1,table2,on="name")
print(fusion)

#TODO : Practice
table3 = table1+table2
print(table3)
