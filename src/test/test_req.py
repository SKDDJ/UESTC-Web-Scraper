# # 导入 requests 包
# import requests

# # 发送请求
# # x = requests.get('https://www.runoob.com/')
# # x = requests.get('https://google.com')
# x = requests.get('https://baidu.com')


# # 返回网页内容
# # print(x.text)
# print(x.json)

import requests 

# x = requests.get('https://news.uestc.edu.cn/?n=UestcNews.Front.CategoryV2.Page&CatId=50')

# x = requests.get('https://study.uestc.cn/toutiao/#/')
x = requests.get('https://shiym.top')

print(x.text)