# -*- coding: utf-8 -*-\

# 반복문

## for 문

## for 반복변수 in 리스트|튜플|문자열:
## 실행할 명령문 1
## 실행할 명령문 2

test_list = ['one', 'two', 'three']
for i in test_list:
  x = i + '!'
  print x ## one! two! three!

number = 0
for score in [90, 25, 67, 45, 93]:
  number += 1
  if score >= 60:
    print('%d번 학생은 합격입니다.' %number)
  else:
    print('%d번 학생은 불합격입니다.' %number)

## while 문
## while 조건식:
##  실행할 명령문1
##  실행할 명령문2
i = 0
while i < 5:
  i += 1
  print('*' * i)
