import json
import requests

url = "http://localhost:5000/empdb/employee"

response = requests.get(url)

# 打印状态码
print(response.status_code)

# json格式打印get内容
print(response.text)

# post 一条数据
data = {"id":"301", "name":"zhaoran", "title":"hello"}
res = requests.post(url,json=data)

# 删除id为201的数据
res = requests.delete(url,201)

