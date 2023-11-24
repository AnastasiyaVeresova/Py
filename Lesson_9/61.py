# 1. Определить какое максимальное и минимальное значение median_house_value 2. Показать максимальное median_house_value, где median_income = 3.1250 3. Узнать какая максимальная population в зоне минимального значения median_house_value

import pandas as pd

# Задача №61. Решение в группах
# 1. Определить какое максимальное и минимальное значение median_house_value
# print(df.median_house_value.max())

file = 'california_housing_train.csv'

df = pd.read_csv(file)

print(df[['median_house_value']].max())
print(df[['median_house_value']].min())
print(df[['median_house_value']].mean())  # среднее
print(df[['median_house_value']].median())  # медианное


# 2. Показать максимальное median_house_value, где median_income = 3.1250
print(df.loc[df.median_income == 3.1250, ['median_house_value']].max())

# 3. Узнать какая максимальная population в зоне минимального значения median_house_value
print(df.median_house_value.min())  # 14999.0
# min_ = df.median_house_value.min()
print(df.loc[df.median_house_value == df.median_house_value.min(), ['median_house_value', 'population']])
# df.loc[df.median_house_value == df.median_house_value.quantile(0.15)]
print('median_house_value.quantile:')
print(df.median_house_value.quantile(0.05))
print(df.loc[df.median_house_value < df.median_house_value.quantile(0.05), ['median_house_value', 'population']])
df_min_val = df.loc[df.median_house_value < df.median_house_value.quantile(0.05)]
print(df_min_val.population.max())
