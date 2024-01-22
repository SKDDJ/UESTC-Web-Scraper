import random

import requests
import pandas as pd
import time


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
        return "Error: " + str(response.status_code)


def main():
    total = 10460
    pageSize = 10
    sleep_time = random.random()
    time.sleep(sleep_time)
    if total // pageSize == total / pageSize:
        pages = total // pageSize
    else:
        pages = total // pageSize + 1

    df = pd.DataFrame(columns=["id", "title", "sourceUrl", "addTime"])
    count_save = 0
    for index in range(1, pages + 1):
        data = fetch_data(index, pageSize)
        json_data = data["data"]
        for item in json_data:
            id = item["id"]
            title = item["title"]
            sourceUrl = item["sourceUrl"]
            addTime = item["addTime"]
            df.loc[len(df)] = [id, title, sourceUrl, addTime]
        if count_save == 100:
            count_save = 0
            df.to_csv(f"./output_{count_save}.csv")
        count_save += 1

    df.to_csv("./output.csv")
    print("爬取完成！")


if __name__ == "__main__":
    main()
