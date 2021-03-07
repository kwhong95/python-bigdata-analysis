# -*- coding: utf-8 -*-

# 함수 정의

# 1. 사용자 정의 함수
## 인수 개수가 정해진 경우
def sum1(a, b):
  x = a + b
  return x
  
## 인수 개수가 정해지지 않은 경우
def sum2(*args):
  x = 0
  for i in args:
    x += i
  return x ## backspace로 for 와 위치를 맞춰줘야 정상 작동

# 함수 호출
a = 5
b = 3

print(sum1(a, b)) ## 8
print(sum1(3, 5)) ## 8
 
print(sum2(1,2,3,4,5)) 
print(sum2(2, 3.5, 10))

# 2. 내장 함수

## abs(x) : 숫자 x의 절대값을 반환
print(abs(-3.5)) 

## all(iterable_x) : 그룹 자료형의 변수 x의 모든 원소가 참이면(0이 아닌 값) True를 반환
print(all([1, 2, 3, 4]))
print(all([4, -2, 0.0, 4]))

## any(iterable_x) : 그룹 자료형의 변수 x의 원소 중 하나라도 참이면 True를 반환
print(any([1, 2, 3, 4]))
print(any([4, -2, 0.0, 4]))

## chr(x) : 아스키코드 값 x에 대한 문자 출력
print(chr(97))
print(chr(48))

## ord(c) : 문자 c에 대한 아스키코드 값 출력
print(ord('a'))
print(ord('0'))

## dir(x) : 객체 x가 가진 맴버 변수와 맴버 함수 보여주기
print(dir([1, 2, 3]))
print(dir({'1' : 'a'}))
print(dir(1))

## divmod(a, b) : a를 b로 나눈 몫과 나머지를 튜플로 반환
print(divmod(7, 3))
print(divmod(1.3, 0.2))

## oct(x) : 정수값 x를 8진수로 변환하여 반환
print(oct(8))
print(oct(234))

## hex(x) : 정수값 x를 16진수로 변환하여 반환
print(hex(16))
print(hex(234))

## id(obj) : obj(객체)의 주소값을 반환
a = 3
print(id(a))

## int(x) : x를 정수 형태로 반환
print(int('3'))

## str(x) : x를 문자열 형태로 반환
print(str(3))

## list(x) : x를 리스트로 반환
print(list('Python'))
print(list((1, 2, 3)))

## tuple(x) : x를 튜플로 반환
print(tuple('Python'))
print(tuple([1, 2, 3]))

## type(x) : x의 자료형을 반환
print(type('abc'))
print(type(a))

## lambda : 간단한 삽입형 함수 생성
sum = lambda a, b: a+b
print(sum) 
print(sum(3, 5))

## max(iterable_x) : 반복 기능한 그룹 자료형 x를 입력받은 뒤 최대값을 반환 
print(max([1, 4, 2, 8, 6]))
print(max('Python'))

## min(iterable_x) : 반복 가능한 그룹 자료형 x를 입력받은 뒤 최소값을 반환
print(min([1, 4, 2, 8, 6]))
print(min('Python'))

## pow(x, y) : x의 y 제곱 결과값 반환
print(pow(2, 4))

## input() : 사용자 입력으로 받은 값을 문자열로 반환
c = input()
print(c) 
c = input('정수를 입력하세요: ')
print(c)

## range(x) : 입력받은 수자에 해당되는 범위의 값을 반환
print(range(5))
print(list(range(5)))
print(list(range(5, 10)))
print(list(range(5, 10, 2)))

## len(s) : 입력값 s의 길이를 반환
print(len('Python'))

## sorted(iterable_x) : 입력값을 정렬하여 리스트로 반환
print(sorted([3, 0, 2, 1]))
print(sorted('Python'))

# 3. 모듈과 패키지
#Request('http://www.hanb.co.kr')
## NameError: name 'Request' is not defined
## 기본 내장 함수가 아닌 Request 함수를 그냥 사용하면 에러 발생!

import urllib.request
print(urllib.request.Request('http://www.hanb.co.kr'))

import pandas 
print(pandas.DataFrame())

from datatime import datetime 
print(datatime.now())