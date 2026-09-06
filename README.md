# urllib3_GET_POST
urllib3_GET\POST方法例程
# GET.PY
~~~~~~
urllib3.disable_warnings()               # 关闭ssl警告
jingdong_url = 'https://www.jd.com/'     # 京东url地址
python_url = 'https://www.python.org/'   # Python url地址
baidu_url = 'https://www.baidu.com/'     # 百度url地址
http = urllib3.PoolManager()             # 创建连接池管理对象
r1 = http.request('GET',jingdong_url)    # 向京东地址发送GET请求
r2 = http.request('GET',python_url)      # 向python地址发送GET请求
r3 = http.request('GET',baidu_url)       # 向百度地址发送GET请求
print('京东请求状态码：',r1.status)
print('python请求状态码：',r2.status)
print('百度请求状态码：',r3.status)
~~~~~~
## 输出
  京东请求状态码： 200   
  python请求状态码： 200   
  百度请求状态码： 200   

# POST.PY
~~~~
import urllib3    # 导入urllib3模块
urllib3.disable_warnings()               # 关闭ssl警告
url = 'https://www.httpbin.org/post'    # post请求测试地址
params = {'name':'Jack','country':'中国','age':30}  # 定义字典类型的请求参数
http = urllib3.PoolManager()             # 创建连接池管理对象
r = http.request('POST',url,fields=params)    # 发送POST请求
print('返回结果：',r.data.decode('utf-8'))
~~~~
## 输出  

返回结果：    
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "age": "30", 
    "country": "\u4e2d\u56fd", 
    "name": "Jack"
  }, 
  "headers": {
    "Accept-Encoding": "identity", 
    "Content-Length": "307", 
    "Content-Type": "multipart/form-data; boundary=7b2659137c805605268c8f6829d334bf", 
    "Host": "www.httpbin.org", 
    "User-Agent": "python-urllib3/2.5.0", 
    "X-Amzn-Trace-Id": "Root=1-6a9d3974-1e496b4b74166d564e822817"
  }, 
  "json": null, 
  "origin": "111.60.88.224", 
  "url": "https://www.httpbin.org/post"
}   

