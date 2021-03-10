from bs4 import BeautifulSoup

html = '<h1 id="title">한빛출판네트워크</h1><div class="top"><ul><li><a href="http://www.hanbit.co.kr/member/login.html" class="login">로그인</a></li></ul><ul class="brand"><li><a href="http://hanbit.co.kr/media/">한빛 미디어</a></li><li><a href="http://hanbit.co.kr/academy/">한빛아카데미</a></li></ul></div>'
  
soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())

print(soup.h1)

tag_h1 = soup.h1
print(tag_h1)

tag_div = soup.div
print(tag_div)

tag_ul = soup.ul
print(tag_ul)

tag_li = soup.li
print(tag_li)

tag_a = soup.a
print(tag_a)

tag_ul_all = soup.find_all("ul")
print(tag_ul_all)

tag_li_all = soup.find_all("li")
print(tag_li_all)

tag_a_all = soup.find_all("a")
print(tag_a_all)

# 속성 이름과 속성값으로 딕셔너리 구성
print(tag_a.attrs)

# href와 class의 속성값 확인
print(tag_a['href'])
print(tag_a['class'])

# ul 태그 중 class의 속성값이 brand인 것 찾기
tag_ul_2 = soup.find('ul', attrs={'class': 'brand'})
print(tag_ul_2)

# id 속성값이 'title'인 것 찾기
title = soup.find(id = 'title')
print(title)
print(title.string)

# div 태그 블록 안에서 ul태그의 class 속성값이 brand인 블록 안의 li 태그 블록을 모두 추출
li_list = soup.select("div>ul.brand>li")
print(li_list)

# li 태그 블록에 있는 문자열 출력
for li in li_list:
  print(li.string)

  