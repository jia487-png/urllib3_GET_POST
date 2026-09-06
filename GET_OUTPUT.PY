import urllib3    # 导入urllib3模块
urllib3.disable_warnings()               # 关闭ssl警告
url = 'https://www.httpbin.org/get'    # get请求测试地址
http = urllib3.PoolManager()             # 创建连接池管理对象
r = http.request('GET',url)              # 发送GET请求,默认重试请求
response_header = r.info()               # 获取响应头
for key in response_header.keys():      # 循环遍历打印响应头信息
    print(key,':',response_header.get(key))