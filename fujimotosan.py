import pandas as pd

df = pd.DataFrame({'name': ['A', 'B', 'C', 'D'],
                   'age': [25, 35, 20, 30]})

df_first = pd.DataFrame({'name': ['A', 'B', 'C', 'D'],
                         'age': [25, 35, 20, 30]})

# df: アクセス数データが入ったDataFrame　 'date'列を日付型に変換
df['date'] = pd.to_datetime(df['date'])

# 1. 月ごとにデータをグループ化し、最初の行＝各グループ内で月の初日を求める
df['first'] = df.groupby(df['date'].dt.to_period('M'))['date'].transform('first') == df['date']

# 2. 月別変化(差分）の把握（月の初日だけのデータフレームを作成済み）
df_first['difference'] = df_first.groupby('title')['pv'].diff().fillna(0)

# 各 title の最初の行(一番初めの月）は、当月の 'pv' 値を代入なども前処理を行って可能
df_first.loc[first_row_mask, 'difference'] = df_first['pv']
