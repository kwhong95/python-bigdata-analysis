# -*- coding: utf-8 -*-\
# 조건문

## if 문
x = 10
if x == 10:
  print('x는 10입니다')

## elif
x = 20 
if x == 10:
  print('x는 10입니다')
elif x == 20:
  print('x는 20입니다')

## else
x == 9
if x == 10:
  print('x는 10입니다')
else:
  print('x는 10이 아닙니다')

# EXAMPLE
num = int(input('0~ 100 안에서 숫자 하나를 입력 해주세요:'))

if num < 10:
  print('입력값은 10보다 작습니다')
elif num > 10 and num <= 50:
  print('입력값은 10보다 크고 50보다 같거나 작습니다')
elif num > 51 and num <= 100:
  print('입력값은 51보다 크고 100보다 같거나 작습니다')
else:
  print('입력값이 범위내에 포함되지 않습니다')

# 비교 연산자
x = 3
y = 2
print(x == y) # False
print(x != y) # True
print(x >= y) # True

# 조건의 연결 
money = 1300
if money >= 1200 and money < 3500:
  print('버스를 탈 수 있습니다.')

# 그룹 자료형의 원소인지 검사하기
print(1 in [1, 2, 3]) # True
print(x in [1, 2, 3]) # True
print(x not in [1, 2, 3]) # False
print('a' in ('a', 'b', 'c', 'd')) # True
print('i' not in 'Python') # True

# 아무 것도 하지 않게 설정 ( pass )
if money < 10:
  pass
else: 
  print('저금하자!')