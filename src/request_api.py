import requests
import json
import logging
from datetime import datetime

current_time = datetime.now().strftime("%m-%d-%H-%M")
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s -   %(message)s",
    datefmt="%Y/%m/%d %H:%M:%S",
    level=logging.INFO,
    filename=f'../logs/{current_time}-api.log'
)

def fetch_data():
    url = "https://vlab.uestc.edu.cn/api/api/toutiao/querytoutiaolist"
    params = {
        'title': '',
        'source': 0,
        'pageIndex': 1,
        'pageSize': 10
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return "Error: " + str(response.status_code)
        
def save_data_to_json(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)
        
def main():
    data = fetch_data()
    save_data_to_json(data, 'data.json')
    # print("Data saved to data.json")
    logging.info("Data saved to data.json")


if __name__ == "__main__":
    main()
