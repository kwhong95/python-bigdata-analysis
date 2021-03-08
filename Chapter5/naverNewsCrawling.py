# -*- coding: utf-8 -*-\

# 전체 작업 스토리 설계
def main():
  node = 'news' # 크롤링할 대상
  srcText = input('검색어를 입력하세요: ')
  cnt = 0
  jsonResult = []

  jsonResponse = getNaverSearch(node, srcText, 1, 100) # [CODE2]
  total = jsonResponse['total']

  while ((jsonResponse != None) and (jsonResponse['display'] != 0)):
    for post in jsonResponse['items']:
      cnt += 1
      getPostData(post, jsonResult, cnt) #[CODE 3]

  start = jsonResponse['start'] + jsonResponse['display']
  jsonResponse = getNaverSearch(node, srcText, start, 100) #[CODE 2]

print('전체 검색: %d 건' %total)

with open('%s_naver_%s.json' % (srcText, node), 'w', encoding = 'utf-8')
          as outfile:
        jsonFile = json.dumps(jsonResult, indent = 4, sort_keys = True,
                              ensure_ascii = False)
        
        outfile.write(jsonFile)
print("가져온 데이터: %d 건" %(cnt))
print('%s_naver_%s.json SAVED' % (srcText, node))

# url 접속 요청 및 응답 후 반환
def getRequestUrl(url):
  req = urllib.request.Request(url)
  req.add_header("X-Naver-Client-Id", client_id)
  req.add_header("X-Naver-Client-Secret", client_secret)

  try:
    response = urllib.request.urlopen(req)
    if response.getccode() == 200:
      print('[%s] Url Request Success' %datatime.datatime.now())
      return response.read().decode('utf-8')
  except Exception as e:
    print(e)
    print("[%s]Error for URL : %s" % (datatime.datatime.now(), url))
    return None

