# -*- coding: utf-8 -*-\

# 튜플 자료형 
## 원소를 순서대로 나열한 그룹 자료형
## 리스트와 달리 원소의 값을 변경할 수 없음

# 튜플 만들기
t1 = (1, )
t2 = (1, 2, 3)
t3 = 1, 2, 3
t4 = (1, 2, (3, 4), ('Life', 'is'))

# 튜플 인덱싱 
print(t4[0]) # 1
print(t4[3][-1]) # 'is'

# 튜플 슬라이싱
print(t4[0:3]) # (1, 2, (3, 4))

# 튜플 연결 ( + )
print(t1 + t2) # (1, 1, 2, 3)
# print(t1 + ' hi ~ ^^;') TypeError: can only concatenate tuple (not "str") to tuple
## 튜플과 문자열은 연결이 불가능하므로 에러 메세지 출력!

# 튜플 반복 ( * )
print(t2 * 3) ## (1, 2, 3, 1, 2, 3, 1, 2, 3)

# 튜플 수정 ( 불가능 )
# t2[2] = 99 TypeError: 'tuple' object does not support item assignment
## 튜플은 수정이 불가능 하므로 에러 메세지 출력