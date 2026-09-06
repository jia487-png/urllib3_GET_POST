import urllib3    # 导入urllib3模块
urllib3.disable_warnings()               # 关闭ssl警告
url = 'https://www.httpbin.org/post'    # post请求测试地址
params = {'name':'Jack','country':'中国','age':30}  # 定义字典类型的请求参数
http = urllib3.PoolManager()             # 创建连接池管理对象
r = http.request('POST',url,fields=params)    # 发送POST请求
print('返回结果：',r.data.decode('utf-8'))