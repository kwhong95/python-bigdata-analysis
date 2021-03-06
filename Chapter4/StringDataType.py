# -*- coding: utf-8 -*-\
# 문자열 연결
head = "Python"
tail = " is Fun"
print(head + tail)

# 문자열 곱하기
print(head * 2)
print("=" * 5)

# 문자열 인덱싱
a = "Now is better than never"
print(a[0]) 
print(a[4])
print(a[-1])
print(a[-2])

# 문자열 슬라이싱
b = a[0] + a[1] + a[2]
print(b)
print(a[0 : 3])
print(a[4 : 6])
print(a[19:])
print(a[:3])
print(a[:])
print(a[7 : -11])

# 문자 개수 계산 ( count() )
a = "Python"
print(a.count("p"))

# 문자 위치 확인( find(), index() )
a.find('y')
a.find('p')  # 없으면 -1 출력
a.index('y')
# a.index('p')  ValueError : substring not found

# 문자 삽입 ( join() )
b = ','
c = b.join('Abcd')
print(c)

# 대문자 변환
print(a.upper())

# 소문자 변환
print(a.lower())

# 공백 제거
d = "       py       "
print(d.lstrip())
print(d.rstrip())
print(d.strip())

# 문자열 수정 (불가능)
a = 'Pithon'
# a[1] = "y" Type Error: 'str' object does not support item assignment

# 문자열 바꾸기
a = 'Python is difficult.'
print(a.replace('difficult', 'funny'))

# 문자열 나누기
print(a.split())

b = 'a, b, c, d'
print(b.split(','))