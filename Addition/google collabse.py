name_2 = input('Введите новое имя абонента ')
        phone_book[name_2] = phone_book.pop(name_1)
        print(f'Контакт успешно изменен \n{phone_book[name_2]}')

-----------------------------------------------------------
dict.pop(key[, default]) - удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение).

---------------------------------------------

df.loc[     df['median_income'] < 2,   ['median_house_value'], [0,2]   ]

------------------------------------------------
df.loc[     (df['housing_median_age'] < 20) & (df['median_house_value'] > 70000),   ['housing_median_age', 'median_house_value']   ]

--------------------------------------------------------------------------
Задача №61. Решение в группах
1. Определить какое максимальное и минимальное
значение median_house_value
2. Показать максимальное median_house_value, где
median_income = 3.1250
3. Узнать какая максимальная population в зоне
минимального значения median_house_value

print(df['population'].max())

-------------------------------------------------
# Максимальное значение
print(df['median_house_value'].max())
# Минимальное значение
print(df['median_house_value'].min())

---------------------------------------

print(df['median_house_value'].max(), df['median_house_value'].min())

----------------------------------------
df.loc[     (df['median_house_value'] == df['median_house_value'].min()),   ['population']  ].max()


-----------------------------------------------------------------
