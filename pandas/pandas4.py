import pandas as pd

food1 = {'number':[1,2,3,4,5],'name':['apple','banana','mangoes','popcorn','pizza'],'price':[3,6,9,12,15]}
food2 = {'color':['red','yellow','green','blue','white'],'weight':[2,3,4,5,6],'quantity':[20,11,33,41,32]}

table1 = pd.DataFrame(food1)
table2 = pd.DataFrame(food2)

fusion = table1.join(table2)
print(fusion)
