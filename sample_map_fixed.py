import pandas as pd

# 年齢ごとに特定の値をマッピングする辞書
age_map = {20: 1000, 30: 2000, 40: 3000}

df = pd.DataFrame({'name': ['A', 'B', 'C', 'D', 'E'],
                   'age': [25, 35, 20, 30, 45]})


# 年齢に対応するボーナスを取得する関数
def get_bonus(x):
    for age in sorted(age_map.keys(), reverse=True):
        if x >= age:
            return age_map[age]
    return 0


# 年齢に対応するボーナスを取得し、新しい列として追加
df['bonus'] = df['age'].apply(get_bonus)

print(df)
