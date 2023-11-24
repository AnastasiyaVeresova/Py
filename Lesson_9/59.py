
import pandas as pd

file = 'california_housing_train.csv'

df = pd.read_csv(file)

# Задача №59. Решение в группах
# 1. Проверить есть ли в файле пустые значения
print(df.isnull().sum())
# 2. Показать median_house_value где median_income < 2
print(df.loc[df.median_income < 2, ['median_income', 'median_house_value']])
# 3. Показать данные в первых 2 столбцах
print(df[['longitude', 'latitude']])
print(df.iloc[:, 0:2])
# 4. Выбрать данные где housing_median_age < 20 и median_house_value > 70000
print(df.loc[df.housing_median_age < 20, ['housing_median_age', 'median_house_value']])
# [4826 rows x 2 columns]
print(df.loc[(df.housing_median_age < 20) & (df.median_house_value > 70000), ['housing_median_age', 'median_house_value']])
    

# df.to_excel('file.xlsx')
# print('*' * 25)
# df2 = df.iloc[:, 0:2]
# print(df2.head())
# print(df2.shape)
# df2.to_excel('file2.xlsx')
# df2.to_csv('df2.csv')