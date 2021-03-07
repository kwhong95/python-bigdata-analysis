# -*- coding: utf-8 -*-\

# 파이썬 프로그래밍 기초 - 연습문제 풀이

## 1. 실행 결과를 참고하여 파이썬 코드 빈칸 채우기
str = '20201231Thursday'
year = str[0:4]
print(year)

# '2020'

mmdd = str[4:8]
print(mmdd)

# '1231'

day = str[8:]
print(day)

# 'Thursday'

## 2. 파이썬 코드의 실행 결과인 a를 예측
a = ['쓰', '레', '기', '통']
a.reverse()
print(a)

# ['통', '기', '레', '쓰']

## 3. 실행 결과를 참고하여 빈칸에 딕셔너리 객체를 선언하는 명령어를 작성

dic = {'year': 2020, 'mm': 12, 'dd': 31, 'day': 'Thursday', 'weather': 'snow'}

print(dic.keys())
# dict_keys(['year', 'mm', 'dd', 'day', 'weather'])
print(dic.values())
# dict_values([2020, 12, 31, 'Thursday', 'snow'])


## 4. 다음 중에서 *틀린* 내용은?
# 1) 문자열은 원소를 변경할 수 없다
# 2) 딕셔너리는 인덱스를 이용하여 슬라이싱을 할 수 있다.
# 3) 튜플은 원소를 변경할 수 없다.
# 4) 집합은 중복 원소를 가질 수 없다.

## 정답: 2) => 딕셔너리는 인덱스 시용이 불가능.

## 5. 실행 결과를 참고하여 빈칸에 이중 for문을 사용한 명령어를 작성
# 반복문
i = 0
while i < 5:
  i += 1
  print('*' * i)

# *
# **
# ***
# ****
# *****

## 6. 실행 결과를 참고하여 매개변수에 대한 평균을 구한 뒤 출력하는 avg()
## 함수를 파이썬 코드 편집기를 사용하여 작성
# RESERT: Root Folder(default)

def avg(*args):
  x = 0
  for i in args:
    x += i
  return x/len(args)

print(avg(5, 3, 12, 9))
print(avg(2.4, 3.2, 7.3))
print(avg(10, 5))

## 7. 다음의 데이터 테이블 pandas의 DataFrame 자료형으로 저장한 뒤
## CSV 파일에 저장
import pandas as pd

data_df = pd.DataFrame([[500, 690, 1100, 1500, 1990, 1020], [450, 700, 1030, 1650, 2020, 1600],
[520, 820, 1200, 1700, 2300, 2200], [610, 900, 1380, 1850, 2420, 2550]], index = ['first', 'second', 'third', 'fourth'])

data_df.columns = [2015, 2016, 2017, 2018, 2019, 2020]

print(data_df)

data_df.to_csv('QuarterlyData.csv', header = 'False')

## 8. 7번의 데이터를 이용하여 연도별 라인 플롯 차트를 그리기
import matplotlib.pyplot as plt

data_df.plot.line()

plt.title('2015-2020 Quarterly Data')
plt.xlabel('Quarties')
plt.ylabel('sales')
plt.show()