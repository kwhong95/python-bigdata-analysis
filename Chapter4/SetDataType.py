# -*- coding: utf-8 -*-\

# 집합 자료형
## { } 안에 key를 가지고 있는 형태로 수학적 집합을 구현한 자료형
## 집합 자료형의 원소는 중복없이 고유해야 하고 원소들이 숫자를 가지지 않기 때문에 인덱스를 사용할 수 없다

# 집합 만들기
s1 = {1, 2, 'a', 5}
s2 = set([1, 2, 3, 4, 5, 6])
print(s2) ## set([1, 2, 3, 4, 5, 6])
s3 = set([4, 5, 6, 7, 8, 9])

# 교집합 연산 ( $, intersection() )
print(s2 & s3) ## set([4, 5, 6])
print(s2.intersection(s3)) ## set([4, 5, 6])

# 합집합 연산 ( |, union() )
print(s2 | s3) ## set([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(s2.union(s3)) ## set([1, 2, 3, 4, 5, 6, 7, 8, 9])

# 차집합 연산 ( -, difference() )
print(s2 - s3) ## set([1, 2, 3])
print(s2.difference(s3)) ## set([1, 2, 3])

# 원소 한 개 추가 ( add(value) )
s2.add(7)
print(s2) ## set([1, 2, 3, 4, 5, 6, 7])

# 원소 여러 개 추가 ( update() )
s2.update([6, 7, 8, 9, 10])
print(s2) ## set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 특정 원소 제거 ( remove(value) )
s2.remove(7)
print(s2) ## set([1, 2, 3, 4, 5, 6, 8, 9, 10])