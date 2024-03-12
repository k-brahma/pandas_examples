import pandas as pd

# 年齢ごとに特定の値をマッピングする辞書
age_map = {20: 1000, 30: 2000, 40: 3000}

df = pd.DataFrame({'name': ['A', 'B', 'C', 'D'],
                   'age': [25, 35, 20, 30]})


# 年齢に対応するボーナスを取得する関数
def get_bonus(x):
    return x.map(age_map).fillna(0)


# 年齢に対応するボーナスを取得し、新しい列として追加
df['bonus'] = df.groupby('age')['age'].transform(get_bonus)

print(df)
