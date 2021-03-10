# Chapter 06 파이썬 크롤링 - 라이브러리 이용
## 01. 정적 웹 페이지 크롤링
> API가 없는 웹 페이지에서 크롤링을 하려면 웹 페이지의 HTML 구조를 분석한 뒤 필요한  
데이터를 직접 크롤링 한다. HTML 구조를 분석하는 작업을 **HTML 파싱**이라고 하며 
BeautifulSoup 라이브러리를 사용한다.

### 1. 정적 웹페이지 크롤링 준비
1. BeautifulSoup 연습하기 1
```
pip3 install beautifulsoup4
```

```
from bs4 import BeautifulSoup
```

