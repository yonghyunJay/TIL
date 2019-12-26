from Crawler import crawler
import urllib
import json
import datetime as dt

page = map(int, input('검색할 최소페이지 최대페이지의 범위를 입력하세요 : ').split())
page_list = list(page)
page_min = page_list[0]
page_max = page_list[1]

for num in range(page_min, page_max):
    params_query = input('이미지를 저장할 키워드를 입력하세요 : ')
    params = {'page':num, 'size':'80', 'query':params_query}
    query = urllib.parse.urlencode(params)

    site_url = "https://dapi.kakao.com/v2/search/image?" + query

    result = crawler.get(site_url)

    data = json.loads(result)
    documents = data['documents']

    for idx, item in enumerate(documents):
        fname = params_query + '_' + dt.datetime.now().strftime('%y%m%d_') + '%02d.png' % idx
        ok = crawler.download(item['image_url'], filename=fname)
        print(ok + '(이)가 저장되었습니다.')