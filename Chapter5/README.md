# Chapter 05 파이썬 크롤링 - API 이용
## 01. 네이버 API를 이용한 크롤링

### 1. 크롤링이란
> 데이터가 가장 많이 존재하는 곳이 SNS를 포함한 인터넷이므로 데이터 수집장소는 대부분 인터넷이다. 다양한 데이터를 쉽고 빠르게 실시간으로 수집 가능  
데이터를 수집하는 기술에는 스크레이핑과 크롤링이 있다.  
스크레이핑 : 웹 사이트에서 특정 데이트를 수집하는 것  
크롤링 : 크롤러 또는 스파이더라는 프로그램으로 웹사이트에서 데이터를 추출하는 것  보통 스크레이핑/크롤링을 구분하지 웹에서 데이터를 수집하는 작업을 크롤링이라고 함

#### 웹 API를 이용한 HTTP 요청과 응답

<img width="589" alt="스크린샷 2021-03-08 오전 12 40 49" src="https://user-images.githubusercontent.com/70752848/110245544-067c2f80-7fa7-11eb-9fb1-84a383cce18d.png">

> 웹은 일반적으로 HTTP 통신을 사용한다. 사용자가 데이터를 가지고 있는 서버의 url에 접속하여 수집할 데이터에 HTTP 요청을 하면 서버가 그에 대한 응답을 JSON 또는 XML 형식으로 보내는 방식이다. 이 때 사용하는 것이 웹 API이며, 지도, 검색,주가, 환율 등 다양한 정보를 가지고 있는 웹 사이트의 기능을 외부에서 쉽게 사용할 수 있도록 사용 절차와 규약을 정의한 것

### 2. 네이버 개발자 가입
#### 1️⃣ 네이버 개발자 센터 접속하기
1. [네이버 개발자 센터 주소](https://developers.naver.com) 접속  
- [서비스 API](https://developers.naver.com/products/datalab/) 접속

2. 오픈 API 이용 신청하기 
- 화면 왼쪽의 [서비스 API] 하위메뉴 > [검색]을 선택
- <오픈 API 이용 신청>

3. 애플리케이션 등록하기

4. 애플리케이션 정보 확인하기

5. 검색 API 이용 안내 페이지 확인하기

### 3. 네이버 뉴스 크롤링
> Client ID와 Client Secret를 이용해 네이버 뉴스에서 월드컵 관련 기사를  
크롤링한 뒤 파일에 저장해본다. 먼저 전체 작업을 설계하고 프로그램의 각 구성과  
개별 함수를 설계한 뒤 전체 프로그램을 작성하는 과정으로 진행해보자.

#### 3.1 전체 작업 설계하기
| 작업 설계 | 사용할 코드 |
| --- | --- |
| 1. 검색어 지정하기 | `srcText = "월드컵"` |
| 2. 네이버 뉴스 검색하기 | `getNaverSearch()` |
| 2.1 url 구성하기 | `url = base + node + srcText` |
| 2.2 url 접속과 검색 요청하기 | `urllib.request.urlopen()` |
| 2.3 요청 결과를 응답 JSON으로 받기 | `json.load()` |
| 3. 응답 데이터를 정리하여 리스트에 저장하기 | `getPostData()` |
| 4. 리스트를 JSON 파일로 저장하기 | `json.dumps()` |

-----

#### 3.2 프로그램 구성 설계하기

<img width="749" alt="스크린샷 2021-03-08 오전 1 23 10" src="https://user-images.githubusercontent.com/70752848/110246904-e3ed1500-7fac-11eb-8332-227e6129ea43.png">

-----

#### 3.3 함수 설계하기
1. [CODE 0] 먼저, 전체 작업 스토리를 설계한다.
- **지역 변수**
  + node : 네이버 검색 API에서 검색할 대상 노드
  + srcText : 사용자 입력으로 받은 검색어 저장
  + cnt : 검색 결과 카운트
  + jsonResult : 검색 결과를 정리하여 저장할 리스트 객체
  + jsonResponce : 네이버 뉴스 검색에 대한 응답을 저장하는 객체
  + total : 전체 검색 결과 개수
  + post : 응답받은 검색 결과중에서 한 개를 저장한 객체
  + items : 전체 응답 검색 결과로 내부 항목은 title, originallink, link, descirption, pubData
  + jsonFile : JSON 파일에 저장할 데이터를 담은 객체
- **메서드**
  + input('검색어를 입력하세요: '): 사용자로부터 입력을 받는다.
  + getNaverSearch(node, srcText, 1, 100) : 1부터 100개의 검색 결과를 처리한다.([CODE2])
  + getPostData(): 검색 결과 한 개를 처리한다([CODE2]).
  + json.dump(): 객체를 JSON 형식으로 변환한다.

2. [CODE 1] url 접속을 요청하고 응답을 받아서 반환하는 부분 작성
- **매개 변수**
  + url : 네이버 뉴스 검색('월드컵')에 대한 url
- **지역 변수**
  + req : url 접속 요청(request) 객체
  + app_id : 네이버 개발자로 등록하고 받은 Client ID
  + app_secret : 네이버 개발자로 등록하고 받은 Client Secret
  + response : 네이버 서버에서 받은 응답을 저장하는 객체
- **메서드**
  + `urllib.request.Request()` : urllib 패키지의 request 모듈에 있는 `Request()` 함수로 네이버 서버에 보낼 요청(request) 객체를 생성
  + `Request.add_header()` : 서버에 보내는 요청 객체 헤더 정보를 추가
  + `urllib.request.urlopen()` : 서버에서 받은 응답을 변수에 저장하기 위해 메모리로 가져오는 urllib 패키지의 request 모듈에 있는 함수
  + `response.getcode()` : 요청 처리에 대한 응답 상태를 확인하는 response 객체의 맴버 함수로 상태코드가 200이면 요청 처리 성공을 나타낸다.
  + `datatime.datatime.now()` : 현재 시간을 구하는 함수
  + `response.read().decode('utf-8')`: utf-8 형식으로 문자열 디코딩