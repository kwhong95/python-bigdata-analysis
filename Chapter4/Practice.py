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