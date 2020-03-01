import requests
href='http://wap.cnki.net/touch/web/Journal/Article/JSYW201810037.html'
res=requests.get(href)
print(res.status_code)