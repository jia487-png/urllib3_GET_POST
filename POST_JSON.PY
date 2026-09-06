import urllib3    # 导入urllib3模块
import json       # 导入json模块
urllib3.disable_warnings()               # 关闭ssl警告
url = 'https://www.httpbin.org/post'    # post请求测试地址
params = {'name':'Jack','country':'中国','age':30}  # 定义字典类型的请求参数
http = urllib3.PoolManager()             # 创建连接池管理对象
r = http.request('POST',url,fields=params)    # 发送POST请求
j = json.loads(r.data.decode('unicode_escape'))  # 将响应数据转换为字典类型
print('数据类型：',type(j))
print('获取form对应的数据：',j.get('form'))
print('获取country对应的数据：',j.get('form').get('country'))
