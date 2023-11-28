import pandas as pd
import random
import numpy as np

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
# print(data)


# name_one = ['robot', 'human']
# name_two = ['1', '0']
# list = list(zip(name_one, name_two))

# print(list)

# dframe = pd.DataFrame(list, columns = ['robot', 'human'])
# print(dframe)


# d = {'robot' : pd.Series([0], index = [0]), 'human': pd.Series([1], index = [1])}
# dframe = pd.DataFrame(d)
# print(dframe)

# data = {
#     'robot' : ['0'],
#     'human' : ['1']
#     }
# row_labels = [0, 1]

# df = pd.DataFrame(data=data, index = row_labels)
# print(df)

# data.loc[data['WhoAmI']] == 'human', 'human' = '1'
# data.loc[data['WhoAmI']] == 'robot', 'robot' = '0'
# data.drop(columns='"WhoAmI')

# data = pd.DataFrame(random.sample(['robot', 'human'] * 10, 10), columns = {'WhoAmI'})
# data.head()
# print(data)

# data = pd.DataFrame(np.arrange(16).reshape(4, 4), index = list('0', '1'), columns = list('robot', 'human'))
# print(data)
#--------------------------------------
# df1 = pd.DataFrame({'robot': [random.randint(0, 1)]})
# df2 = pd.DataFrame({'human': [random.randint(0, 1)]})


# df1.merge(df2, how='cross')

# print(df1)
#---------------------------------
data = {
    'robot' : [0],
    'human' : [1],
    }

row_labels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

df = pd.DataFrame(data=data, index = row_labels)
print(df)
