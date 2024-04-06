from decimal import Decimal

import pandas as pd

# サンプルデータの作成
data = {
    'title': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'pv': [10, 15, 20, 5, 12, 18, 30, 30, 35]
}

# DataFrameの作成
df_first = pd.DataFrame(data)

df_first['difference'] = df_first.groupby('title')['pv'].diff().fillna(0)
df_first['decimail'] = df_first['difference'].apply(lambda x: Decimal(str(x)))

print(df_first)
#
# print(df_first.dtypes)
#
# print(df_first.info())
#
# print(df_first.describe())
