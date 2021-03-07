# -*- coding: utf-8 -*-\
# 1. numpy
import numpy as np
np.__version__

## 리스트를 이용하여 numpy 생성
ar1 = np.array([1, 2, 3, 4, 5])
print(ar1)

print(type(ar1))

ar2 = np.array([[10, 20, 30], [40, 50, 60]])
print(ar2)

## 값의 범위를 지정하여 numpy 생성 > np.arange(시작값, 끝값, 간격)
ar3 = np.arange(1, 11, 2)
print(ar3)

## 구조를 지정하여 numpy 생성 > np.array().reshape()
ar4 = np.array([1, 2, 3, 4, 5, 6]).reshape((3, 2))
print(ar4)

## 초기값과 구조를 지정하여 numpy 생성
ar5 = np.zeros((2, 3)) # 0으로 초기화하고 2행 3열 구조를 생성
print(ar5)

## numpy 슬라이싱 
ar6 = ar2[0:2, 0:2]
print(ar6)

ar7 = ar2[0, :] # 0행의 모든 열을 슬라이싱
print(ar7)

## numpy 사칙 연산
ar8 = ar1 + 10
print(ar8)
print(ar1 + ar8)
print(ar8 - ar1)
print(ar1 * 2)
print(ar1 / 2) 

## numpy 행렬곱 계산
ar9 = np.dot(ar2, ar4)
print(ar9)

# pandas

## pandas 임포트
import pandas as pd

## pandas 버전 확인
print(pd.__version__)

# Series 자료형

## Series 생성
data1 = [10, 20, 30, 40, 50]
print(data1)

data2 = ['1반', '2반', '3반', '4반', '5반']
print(data2)

## 리스트 이용하여 Series 생성
sr1 = pd.Series(data1)
print(sr1)

sr2 = pd.Series(data2)
print(sr2)

## 값을 이용하여 Series 생성
sr3 = pd.Series([101, 102, 103, 104, 105])
print(sr3)

sr4 = pd.Series(['월', '화', '수', '목', '금'])
print(sr4)

## 인덱스를 지정하여 Series를 생성
sr5 = pd.Series(data1, index=[1000, 1001, 1002, 1003, 1004])
print(sr5)

sr6 = pd.Series(data1, index = data2)
print(sr6)

sr7 = pd.Series(data2, index = data1)
print(sr7)

sr8 = pd.Series(data2, index = sr4)
print(sr8)

## Series 인덱싱
print(sr8[2])
print(sr8['수'])
print(sr8[-1])

## Series 슬라이싱
print(sr8[0:4])

## Series 값 구하기
print(sr8.values)

## Series 원소가 숫자이면 덧셈 수행
print(sr1 + sr3) # 주의: +연산 두 Series 원소의 자료형이 같아야 수행

## Series 원소가 문자열이면 문자열 연결 수행
print(sr4 + sr2)

# DataFrame 자료형

## DataFrame 생성
data_dic = {
  'year': [2018, 2019, 2020],
  'sales': [350, 480, 1099]
}

print(data_dic)

## 딕셔너리 이용하여 DataFrame 생성
df1 = pd.DataFrame(data_dic)

print(df1)

## 리스트를 이용하여 DataFrame 생성 1
df2 = pd.DataFrame([[89.2, 92.5, 90.8], [92.8, 89.9, 95.2]],
index = ['중간고사', '기말고사'], columns = data2[0:3])

print(df2)

## 리스트를 이용하여 DataFrame 생성 2
data_df = [['20201101', 'Hong', '90', '95'], ['20201102',
'Kim', '93', '94'], ['20201103', 'Lee', '87', '97']]
df3 = pd.DataFrame(data_df)

print(df3)

## DataFrame 열 이름 설정
df3.columns = ['학번', '이름', '중간고사', '기말고사']
print(df3)

## DataFrame 조회
print(df3.head(2))
print(df3.tail(2))
print(df3['이름'])

## CSV 파일로 저장
df3.to_csv('score.csv', header = 'False')

## CSV 파일을 DataFrame으로 불러오기
df4 = pd.read_csv('score.csv',
encoding='utf-8', index_col = 0, engine='python')

print(df4)

# 3. matplotlib

## matplotlib 임포트
import matplotlib

## matplotlib 버전 확인
print(matplotlib.__version__)

## pyplot 모듈 임포트하기
import matplotlib.pyplot as plt

# 라인 플롯 차트 그리기
## 1. 데이터 준비
x = [2017, 2018, 2019, 2020, 2021]
y = [350, 410, 520, 695, 543]

## 2. x축과 y축 데이터를 지정하여 라인플롯 생성
plt.plot(x,y)

## 3. 차트 제목 설정
plt.title('Annual sales')

## 4. x축 레이블 설정
plt.xlabel('years')

## 5. y축 레이블 설정
plt.ylabel('sales')

## 6. 라인 플롯 표시
print(plt.show())

# 바 차트 그리기
## 1. 데이터 준비
y1 = [350, 410, 520, 695]
y2 = [200, 250, 385, 350]
x = range(len(y1))

## 2. x축과 y축 데이터를 지정하여 바 차트 생성
plt.bar(x, y1, width = 0.7, color = 'blue')
plt.bar(x, y2, width = 0.7, color = 'red', bottom = y1)

## 3. 차트 제목 설정
plt.title('Quarterly sales')

## 4. x축 레이블 설정
plt.xlabel('Quarters')

## 5. y축 레이블 설정
plt.ylabel('sales')

## 6. 눈금 이름 리스트 작성
xLabel = ['first', 'second', 'third', 'fourth']

## 7. 바 차트의 x축 눈금 이름 설정
plt.xticks(x, xLabel, fontsize = 10)

## 8. 범례 설정
plt.legend(['chairs', 'desks'])

## 9. 바 차트 표시
plt.show()

