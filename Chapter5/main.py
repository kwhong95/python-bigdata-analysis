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

print('전체 검색: %d 건' %(cnt))
print('%s_naver_%s.json SAVED' % (srcText, node))

def getRequestUrl(url):
  req = urllib.request.Request(url)
  req.add_header("X-Naver-Client-Id", client_id)
  req.add_header("X-Naver-Client-Secret", client_secret)

  try:
    response = urllib.request.urlopen(req)
    if response.getccode() == 200:
      print('[%s] Url Request Success' %datatime.datatime.now())
      return response.read().decode('utf-8')
  except Exception as :
    print(e)
    print("[%s]Error for URL : %s" % (datatime.datatime.now(), url))
    return None
