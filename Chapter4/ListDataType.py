# -*- coding: utf-8 -*-\
# 리스트 만들기
a = [1, 2, 3]
b = ['Life', 'is', 'too', 'short']
c = [1, 2, 'Life', 'is']
d = [1, 2, [3, 4], ['Life', 'is']]

# 리스트 인덱싱
print(d[0])
print(d[2])
print(d[3])
print(d[3][-1])

# 리스트 슬라이싱 
print(d[0:3])

# 리스트 연결 ( + )
print(a + b)
print(b[0] + " hi~ ^^;")
# print(a[0] + " hi~ ^^;") 타입에러 : a[0]는 int형이므로 문자열과 연결할 수 없다!

# 리스트 반복 ( * )
print(a * 3)

# 리스트 수정
a[2] = 99
print(a)
## 슬라이싱 + 리스트 수정
a[1:2] = ['a', 'b', 'c']
print(a) # [1, 'a', 'b', 'c', 99]
## 인덱스 접근후 리스트 수정
a[-1] = ['d', 'e', 'f']
print(a) # [1, 'a', 'b', 'c', ['d', 'e', 'f']]

# 삭제 ( del )
del a[-1]
print(a)

# 원소 추가 ( append() )
a.append(5)
print(a)

# 원소 정렬 ( sort() )
b.sort()
print(b)

# 원소 순서 뒤집기 ( reverse() )
a = [3, 4, 1, 9]
a.reverse()
print(a) # [9, 1, 4, 3]

# 원소 위치 확인 ( index() )
print(a.index(9)) # 0

# 원소 삽입 ( insert(index, value) )
a.insert(0, 99)
print(a) 

# 원소 삭제 ( remove(value), pop() )
a.remove(99)
print(a) 

b = [1, 2, 3]
b.pop() # 맨 뒤 삭제
print(b)

b.pop(0) # 정의한 index 삭제 가능
print(b) 

# 특정 원소값의 개수 ( count(value) )
a = [2, 1, 0, 2, 3, 2, 4, 2]
print(a.count(2))