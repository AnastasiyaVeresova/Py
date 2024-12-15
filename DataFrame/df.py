import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10

random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

one_hot_dict = {}

for value in data['whoAmI'].unique():
    one_hot_dict[value] = [1 if x == value else 0 for x in data['whoAmI']]

one_hot_data = pd.DataFrame(one_hot_dict)
one_hot_data.head()
print(one_hot_data)
