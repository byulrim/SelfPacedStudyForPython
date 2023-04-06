import pandas as pd

df = pd.read_csv("data/command_data.csv")
df_1 = df.groupby("id").count()
df_1 = df_1.sort_values(by="command", ascending=False)

df_1.rename(columns={"command": "command count"}, inplace=True)

print(df_1.head(10))
