import pandas as pd

document = [
    "코로나 상생지원금 문의입니다.",
    "낮 12시 ~ 2시 지하철 운행시간 문의입니다.",
    "밤 12시 이후 버스 운행시간 문의입니다.",
    "사회적 거리두기로 인한 10시 이후 영업시간 안내입니다.",
    "Bus 운행시간 문의입니다.",
    "Taxi 승강장 문의입니다.",
]

df = pd.DataFrame({"문서": document})

df["날짜"] = pd.date_range("2023-04-08", periods=6)

df_1 = df[df["날짜"] > "2023-04-11"]

print(df_1)
