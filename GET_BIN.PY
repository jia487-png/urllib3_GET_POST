import urllib3    # 导入urllib3模块
urllib3.disable_warnings()               # 关闭ssl警告
url = 'http://sck.rjkflm.com:666/spider/file/python.png'  # 图片请求地址
http = urllib3.PoolManager()             # 创建连接池管理对象
r = http.request('GET',url)              # 发送网络请求
print(r.data)                            # 打印二进制数据
f = open('python.png','wb+')             # 创建open对象
f.write(r.data)                          # 写入数据
f.close()                                # 关闭
