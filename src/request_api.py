import requests

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

def main():
    data = fetch_data()
    print(data)

if __name__ == "__main__":
    main()
