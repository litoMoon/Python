#对百度连接发起请求
import requests

r=requests.get("http://www.baidu.com")

print(r)
print(r.status_code)
print(r.url)
print(r.status_code)
print(r.text)
# 输出：<Response [200]>