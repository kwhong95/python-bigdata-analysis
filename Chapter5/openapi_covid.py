from urllib2 import Request, urlopen
from urllib import urlencode, quote_plus

url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : 'mQ12y4QAfbuZL2fpRcPbVSTKZY%2BoEy6pNjTBVz1wFY6Wd9BEkEJ6a0o85TUBK6o9NXHaF6c%2B6FZ%2BshGbhzAygw%3D%3D', quote_plus('pageNo') : '1', quote_plus('numOfRows') : '10', quote_plus('startCreateDt') : '20200310', quote_plus('endCreateDt') : '20200315' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print(response_body)