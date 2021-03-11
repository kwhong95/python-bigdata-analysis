# Chapter 06 파이썬 크롤링 - 라이브러리 이용
## 01. 정적 웹 페이지 크롤링
> API가 없는 웹 페이지에서 크롤링을 하려면 웹 페이지의 HTML 구조를 분석한 뒤 필요한  
데이터를 직접 크롤링 한다. HTML 구조를 분석하는 작업을 **HTML 파싱**이라고 하며 
BeautifulSoup 라이브러리를 사용한다.

### 1. 정적 웹페이지 크롤링 준비
1. BeautifulSoup 연습하기 1
> HTML Parsing
```
pip3 install beautifulsoup4
```

```
from bs4 import BeautifulSoup
```

```py
soup = BeautifulSoup(html, 'html.parser')
```

2. BeautifulSoup 연습하기 2
> Tag Pasing(코드 참조)

- 1️⃣ `attrs`: 속성 이름과 속성값으로 딕셔너리 구성
- 2️⃣ `find()` : 속성을 이용하여 특정 태그 파싱
- 3️⃣ `select()` : 지정한 태그를 모두 파싱하여 리스트 구성
  + `태그#id 속성값`
  + `태그.class 속성값`

### 2. 정적 웹 페이지 크롤링 실습
#### 1. 크롤링 허용 여부 확인하기
> 웹 페이지 크롤링 전 허용 여부를 확인하기 위해 '크롤링할 주소/robot.txt'를 입력해본다. 수집 정책을 알려주기 위해 사용하며, 파일이 없다면 정책이 없으니 크롤링을 해도 된다는 의미로 받아들이고, 오픈소스, 오픈데이터, 공유 경제 시대인 만큼 강제성이 없더라도 지키며 사용할 것.

#### 2. 웹 페이지 분석하기
> 할리스 커피의 전국 매장 정보 크롤링하기

## 02. 동적 웹 페이지 크롤링

### 1. 동적 웹 페이지 크롤링 준비
```
pip3 install selenium
```
