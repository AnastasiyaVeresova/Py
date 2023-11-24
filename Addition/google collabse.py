
import pandas as pd
import seaborn as sns

df = pd.read_csv('sample_data/california_housing_train.csv')


DataFrame.head(n=5) #прочитать первые n строк таблицы
df[df['housing_median_age'] < 20] #вывести столбец total_rooms, у которого медианный возраст здания(housing_median_age) меньше 20
df[(df['housing_median_age'] > 20) & (df['total_rooms'] > 2000)]#& - выполнение одновременно всех условий. | - выполнение хотя бы одного из условия

#вывести один столбец
df[df['housing_median_age'] < 20, 'total_rooms'] # или (если необходимо вывести 2 и более столбцов df[df['housing_median_age'] < 20, ['total_bedrooms', 'total_rooms']]

print(df['population'].max())#Максимальное значение

print(df['population'].min())#Минимальное значение

print(df['population'].mean())#Среднее значение

print(df['population'].sum())#Сумма

df[['population', 'total_rooms']].median()#Медианное значение для нескольких столбцов

df.describe() #Перцентиль - это показатель, используемый в статистике, показывающий значение, ниже которого падает определенный процент наблюдений в группе наблюдений Получить общую картину можно простой командой
#count - Общее кол-во не пустых строк, mean - среднее значение в столбце std - стандартное отклонение от среднего значения, min - минимальное значение, max - максимальное значение Числа 25%, 50%, 75% - перцентили



df.head()

df.tail()

df.shape  #возвращает размеры таблицы: кортеж из 2 значений, 1 - количество строк, 2 - количество столбцов.

df.isnull() #обнаружить пустые значения в таблице данных 

df.isnull().sum() #выведет количество null-значений в каждой ячейке по столбцам.

df.dtypes #выведет тип данных

df.columns #узнать название всех столбцов в таблице

df['latitude'] #вывести 1 столбец на экран

sns.scatterplot(data=df, x="longitude", y="latitude")#Изображение точек долготы по отношению к широте двумерное

sns.scatterplot(data=df, x="households", y="population",  hue="total_rooms")#цветовое заполнение

sns.relplot(x="latitude", y="median_house_value", kind="line", data=df)#Для генерации линейных графиковЛинейные графики

sns.relplot(x = 'longitude', y = 'median_house_value', kind = 'line', data = df)#анализ соотношенийЛинейные графики

sns.scatterplot(data=df, x="latitude", y="longitude",  hue="median_house_value")
#анализ соотношений(цветовой)Линейные графики

sns.histplot(data=df, x="median_income")#гисторгамма

sns.histplot(data = df, x = 'housing_median_age')#гисторгамма

sns.histplot(data=df[df['housing_median_age']>50], x="median_income") #медианный доход у пожилых жителей

df.loc[df['housing_median_age'] <= 20, 'age_group'] = 'Молодые'
df.loc[(df['housing_median_age'] > 20) & (df['housing_median_age'] <= 50), 'age_group'] = 'Ср. возраст'
df.loc[df['housing_median_age'] > 50, 'age_group'] = 'Пожилые'

df.groupby('age_group')['median_income'].mean().plot(kind='bar')#получить среднее значение

df.loc[df['median_income'] > 6, 'income_group'] = 'rich'
df.loc[df['median_income'] < 6, 'income_group'] = 'everyone_else'
sns.displot(df, x="median_house_value", hue="income_group")#Изобразим дополнительное измерение с помощью оттенка в виде возрастных групп и групп по доходам



#____________________________________________________________________


name_2 = input('Введите новое имя абонента ')
        phone_book[name_2] = phone_book.pop(name_1)
        print(f'Контакт успешно изменен \n{phone_book[name_2]}')

# -----------------------------------------------------------
dict.pop(key[, default]) - удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение).

# ---------------------------------------------

df.loc[     df['median_income'] < 2,   ['median_house_value'], [0,2]   ]

# ------------------------------------------------
df.loc[     (df['housing_median_age'] < 20) & (df['median_house_value'] > 70000),   ['housing_median_age', 'median_house_value']   ]

# --------------------------------------------------------------------------
Задача №61. Решение в группах
1. Определить какое максимальное и минимальное
значение median_house_value
2. Показать максимальное median_house_value, где
median_income = 3.1250
3. Узнать какая максимальная population в зоне
минимального значения median_house_value

print(df['population'].max())

# -------------------------------------------------
# Максимальное значение
print(df['median_house_value'].max())
# Минимальное значение
print(df['median_house_value'].min())

# ---------------------------------------

print(df['median_house_value'].max(), df['median_house_value'].min())

# ----------------------------------------
df.loc[     (df['median_house_value'] == df['median_house_value'].min()),   ['population']  ].max()


# -----------------------------------------------------------------

1: Прыгучий Симулятор Андреевич, ['89763245374']
2: Пузиков Григорий Валерьевич, ['8456734']
3: Колесов Радар Петрович ['89112537658', ' 89213457859'], radar@yandex.ru
4: Овощной Андрей Валентинович, ['89123546756']
5: Колесов Эльдар Петрович ['89112537658', ' 89213457859'], radar@yandex.ru
6: Колесов Эльдар Петрович ['89112537658', ' 89213457859'], radar@yandex.ru