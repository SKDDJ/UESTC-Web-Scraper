"""
web_scraper_project/
│
├── driver/             # 存放浏览器驱动
│
├── src/                # 源代码目录
│   ├── __init__.py     # 使 src 成为一个 Python 包
│   └── scraper.py      # 爬虫脚本
│   └── main.py  # 请求新闻网站 API 返回JSON数据 
│
└── requirements.txt    # 项目依赖
"""

import random
import time
import requests
import pandas as pd
from tqdm import tqdm
import json
import logging
from datetime import datetime

# 日志配置
current_time = datetime.now().strftime("%m-%d-%H-%M")
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s -   %(message)s",
    datefmt="%Y/%m/%d %H:%M:%S",
    level=logging.INFO,
    filename=f'../logs/{current_time}-api.log'
)

def fetch_data(page_index, page_size):
    url = "https://vlab.uestc.edu.cn/api/api/toutiao/querytoutiaolist"
    params = {
        'title': '',
        'source': 0,
        'pageIndex': page_index,
        'pageSize': page_size
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        assert data["success"] == True
        return data
    else:
        logging.error("Error: " + str(response.status_code))  # 使用日志记录错误
        return None

def main():
    total = 10460
    pageSize = 10
    sleep_time = random.random()
    time.sleep(sleep_time)
    # interesting
    if total // pageSize == total / pageSize:
        pages = total // pageSize
    else:
        pages = total // pageSize + 1

    df = pd.DataFrame(columns=["id", "title", "sourceUrl", "addTime"])
    all_data = []  # 添加一个列表来保存所有数据
    count_save = 0

    # 从文件中读取上次保存的 index
    try:
        with open('last_index.txt', 'r') as f:
            start_index = int(f.read())
    except FileNotFoundError:
        start_index = 1

    for index in tqdm(range(start_index, pages + 1)):
        # 在每次请求API之前保存当前的 index
        with open('last_index.txt', 'w') as f:
            f.write(str(index))

        data = fetch_data(index, pageSize)
        if data:
            json_data = data["data"]
            all_data.extend(json_data)  # 将数据添加到 all_data 列表
            for item in json_data:
                id = item["id"]
                title = item["title"]
                sourceUrl = item["sourceUrl"]
                addTime = item["addTime"]
                # 将新的数据行[id, title, sourceUrl, addTime]添加到DataFrame的最后一行
                df.loc[len(df)] = [id, title, sourceUrl, addTime]
            if count_save == 100:
                count_save = 0
                df.to_csv(f"./outputs/{count_save}.csv")
                with open(f'all_data_{index}.json', 'w', encoding='utf-8') as f:  # 将数据保存为 JSON
                    json.dump(all_data, f)
                logging.info(f"Page {index-1} saved to all_data_{index-1}.json")  # 使用日志记录进度
            count_save += 1

    df.to_csv("./outputs/final_output.csv")
    with open('all_data_final.json', 'w', encoding='utf-8') as f:  # 最终将所有数据保存为一个 JSON 文件
        json.dump(all_data, f)
    logging.info("全部数据已保存到 all_data_final.json 和 output.csv")
    print("爬取完成！")

if __name__ == "__main__":
    main()
