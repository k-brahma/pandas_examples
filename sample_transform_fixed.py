import pandas as pd

# 年齢ごとに特定の値をマッピングする辞書
age_map = {"20代未満": 1000, "20代": 2000, "30代": 3000, "40代以上": 4000}

df = pd.DataFrame({'name': ['A', 'B', 'C', 'D', 'E'],
                   'age': [15, 25, 35, 45, 55]})


# 年齢に対応するボーナスを取得する関数
def get_bonus(x):
    if x < 20:
        return age_map["20代未満"]
    elif x < 30:
        return age_map["20代"]
    elif x < 40:
        return age_map["30代"]
    else:
        return age_map["40代以上"]


# 年齢に対応するボーナスを取得し、新しい列として追加
df['bonus'] = df['age'].apply(get_bonus)

print(df)
