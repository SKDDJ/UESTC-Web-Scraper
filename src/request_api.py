"""
web_scraper_project/
│
├── driver/             # 存放浏览器驱动
│
├── src/                # 源代码目录
│   ├── __init__.py     # 使 src 成为一个 Python 包
│   └── scraper.py      # 爬虫脚本
│   └── request_api.py  # 请求新闻网站 API 返回JSON数据 
│
└── requirements.txt    # 项目依赖
"""
import requests
import json
import logging
from datetime import datetime
import time 

current_time = datetime.now().strftime("%m-%d-%H-%M")
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s -   %(message)s",
    datefmt="%Y/%m/%d %H:%M:%S",
    level=logging.INFO,
    filename=f'./logs/{current_time}-api.log'
)

def fetch_all_data():
    url = "https://vlab.uestc.edu.cn/api/api/toutiao/querytoutiaolist"
    page_index = 1
    all_data = []

    while True:
        start_time = time.time()
        params = {
            'title': '',
            'source': 0,
            'pageIndex': page_index,
            'pageSize': 10
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            # 如果data为空，说明没有更多的页面，可以跳出循环
            if not data:
                break
            all_data.extend(data)
            with open(f'all_data_{page_index}.json', 'w', encoding='utf-8') as f:
                json.dump(all_data, f)
            end_time = time.time()
            logging.info(f"Page {page_index} saved to all_data_{page_index}.json, time used: {end_time - start_time} seconds")
            page_index += 1
        else:
            print("Error: " + str(response.status_code))
            break

        
def main():
    # data = fetch_data()
    # save_data_to_json(data, 'data.json')
    # print("Data saved to data.json")
    
    
    fetch_all_data()   
    logging.info("All Data saved to data.json")


if __name__ == "__main__":
    main()
