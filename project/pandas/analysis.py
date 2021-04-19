import pandas as pd

df = pd.read_csv('pokemon_data.csv')

# 상단 3개의 데이터 출력
print(df.head(3))

# 하단 3개의 데이터 출력
print(df.tail(3))

# 엑셀 파일 읽기

df_xslx = pd.read_excel('pokemon_data.xlsx')
print(df_xslx.haed(3))
