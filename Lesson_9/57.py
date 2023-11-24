import pandas as pd

# california_housing_train.csv
file = 'california_housing_train.csv'

# Задача №57. Решение в группах
# 1. Прочесть с помощью pandas файл
# california_housing_test.csv, который находится в папке
# sample_data
df = pd.read_csv(file)

print(df.head())
print(df.tail())
# 2. Посмотреть сколько в нем строк и столбцов
print(df.shape)
# 3. Определить какой тип данных имеют столбцы
print(df.dtypes)




