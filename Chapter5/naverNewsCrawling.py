import os
import ssl
import sys
import urllib.request
import datetime
import time
import json

client_id = 'DFdYL78PkhNIgnvDUnXJ'
client_secret = '6xYcnmY87V'

def getRequestUrl(url):
  req = urllib.request.Request(url)
  req.add_header("X-Naver-Client-Id", client_id)
  req.add_header("X-Naver-Client-Seceret", client_secret)
  context = ssl._create_unverified_context()

  try:
    res = urllib.request.urlopen(req, context=context)
    if res.getcode() == 200:
      print("[%s] Url Request Success" %datetime.datetime.now())
      return res.read().decode('utf-8')
  except Exception as e:
    print(e)
    print("[%s] Error for URL: %s" % (datetime.datetime.now(), url))
    return None

def getNaverSearch(node, srcText, start, display):
  base = "https://openapi.naver.com/v1/search"
  node = '/%s.json' %node
  parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(srcText), start, display)

  url = base + node + parameters
  responseDecode = getRequestUrl(url)

  if (responseDecode == None):
    return None
  else:
    return json.loads(responseDecode)

def getPostData(post, jsonResult, cnt):
  title = post['title']
  description = post['description']
  org_link = post['originallink']
  link = post['link']

  pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S + 0900')
  pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

  jsonResult.append({'cnt': cnt, 'title': title, 'description': description, 'org_link': org_link, 'link': link, 'pDate': pDate})
  return

def main():
  node = 'news'
  srcText = input('검색어를 입력하세요: ')
  cnt = 0
  jsonResult = []
  
  jsonResponse = getNaverSearch(node, srcText, 1, 100)
  total = jsonResponse['total']

  while ((jsonResponse != None) and (jsonResponse['display'] != 0)):
    for post in jsonResponse['items']:
      cnt += 1
      getPostData(post, jsonResult, cnt)

    start = jsonResponse['start'] + jsonResponse['display']
    jsonResponse = getNaverSearch(node, srcText, start, 100)

  print('전체 검색 : %d 건' %total)

  with open('%s_naver_%s.json' % (srcText, node), 'w', encoding='utf8') as outfile:
    jsonFile = json.dumps(jsonResult, indent= 4, sort_keys= True, ensure_ascii= False)

    outfile.write(jsonFile)

  print('가져온 데이터: %d 건' %(cnt))
  print('%s_naver_%s.json SAVED' % (srcText, node))


if __name__ == '__main__':
  main()