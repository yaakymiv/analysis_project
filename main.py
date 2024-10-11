import pandas as pd
from sklearn.datasets import load_iris
import numpy as np

df1 = pd.read_excel('data.xlsx', sheet_name='REPORT_2020_CLEARED')
df2 = pd.read_excel('data.xlsx', sheet_name='REPORT_2022_cleared')
df3 = pd.read_excel('data.xlsx', sheet_name='REPORT_2019_CLEARED')
df4 = pd.read_excel('data.xlsx', sheet_name='REPORT_2021')

dfs = [df1, df2, df3, df4]
new = []

for i in range(4):
    # transposing matrix
    dfs[i].rename(columns={'Unnamed: 0': 'index'}, inplace=True)
    new.append(dfs[i].T)

    # Вибираємо перший запис і робимо його колонками
    new[i].columns = new[i].iloc[0]

    # Вибираємо усі записи окрім першого
    new[i] = new[i].iloc[1:]

    # Оновлюємо індекс
    new[i] = new[i].reset_index()

    # Перейменовуємо індекс на City
    new[i].rename(columns={'index': 'City'}, inplace=True)
    if True in new[i].columns.duplicated():
        new[i] = new[i].loc[:, ~new[i].columns.duplicated()]

years = ['2019', '2020', '2021', '2022']
f = []
for i in range(4):
    new[i]['Year'] = years[i]
    f.append(new[i].reset_index(drop=True))

df = pd.concat(f, ignore_index=True)
df.dropna(how='all', axis=1, inplace=True)

# Replacing Year
cols = df.columns.tolist()

# Remove the "Year" column from its current position
cols.remove('Year')

# Insert the "Year" column back right after "City"
city_index = cols.index('City') + 1
cols.insert(city_index, 'Year')

# Reorder the dataframe
df = df[cols]

df.to_excel('df.xlsx', index=True)