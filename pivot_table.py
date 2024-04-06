import os

import pandas as pd

# カレントディレクトリにあるsample.csvを読み込む
df = pd.read_csv('data/pivot_sample.csv')

# データフレームの内容を表示
# print(df.head())
# print(df.tail())

# 2023-01-01 等の日付の値を元にして "yyyy年mm月" の列を追加
df['年月'] = df['日付'].str[:4] + '年' + df['日付'].str[5:7] + '月'

# print(df.head())
# print(df.tail())

# pivot tagbleを作成 yyyymm ごとに支店ごとの売上金額を集計
pivot_table = df.pivot_table(index='年月', columns='支店', values='売上額', aggfunc='sum')

# pivot tableの内容を表示
print(pivot_table)

# output は .xlsx ファイルに保存
os.makedirs('data/results', exist_ok=True)
pivot_table.to_excel('data/results/pivot_sample_output.xlsx')
