# -*- coding: utf-8 -*-\
# 딕셔너리 자료형
## {} 안에 key: value 쌍의 형태로 이루어진 원소를 가지는 그룹 자료형
## 원소는 순서를 가지지 않으므로 인덱스 대신 key를 이용해 원소를 지정

# 딕셔너리 생성
dic = {'name': 'Hong', 'phone': '01012345678', 'birth': '0922'}

# 원소 추가
dic[1] = 'a'
print(dic) ## {'phone': '01012345678', 'name': 'Hong', 'birth': '0922', 1: 'a'}

dic['pet'] = 'dog'
print(dic) ## {'pet': 'dog', 'phone': '01012345678', 'name': 'Hong', 'birth': '0922', 1: 'a'}

# 원소 삭제
del dic[1]
print(dic)  ## {'pet': 'dog', 'phone': '01012345678', 'name': 'Hong', 'birth': '0922'}

# 원소의 value 구하기
print(dic['pet']) ## 'dog'
print(dic['name']) ## 'Hong'

# key의 리스트 만들기 ( keys() )
print(dic.keys()) ## dict_keys(['pet', 'phone', 'name', 'birth'])
print(list(dic.keys())) ## ['pet', 'phone', 'name', 'birth']

# value의 리스트 만들기  ( values() )
print(dic.values()) ## dict_values('dog', '01012345678', 'Hong', '0922'])
print(list(dic.values())) ## ['dog', '01012345678', 'Hong', '0922']

# key, value 쌍 구하기 ( items() )
print(dic.items()) ## [('pet', 'dog'), ('phone', '01012345678'), ('name', 'Hong'), ('birth', '0922')]

# 원소 삭제 ( clear() )
dic.clear()
print(dic) ##  {}