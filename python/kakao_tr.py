import requests
import json

key = 'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'
url = "https://kapi.kakao.com/v1/translation/translate"
text = '이거 번역 좀 해서 뭐 어떻게 잘 써보고 싶은데 이거 되는거 맞는지요..'

header = {'Authorization' : 'KakaoAK ' + key }
param = {'query' : text, 'src_lang' : 'kr', 'target_lang' : 'en'}

req = requests.get( url, params = param, headers= header).text

json_data = json.dumps(req)

print(json_data)
