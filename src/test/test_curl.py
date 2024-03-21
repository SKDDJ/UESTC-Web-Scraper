
import requests

def main():
    WEBHOOK_URL = "https://open.feishu.cn/open-apis/bot/v2/hook/70d7d8f5-0893-41ba-afc5-3ba1a2fbe486"
    params = {
        "msg_type": "text", # 指定消息类型
        "content": {  # 消息内容主体
        "text": "来了！成功了兄弟们！"
        }
            }

    resp = requests.post(WEBHOOK_URL, json=params)
    resp.raise_for_status()
    result = resp.json()
    if result.get("code") and result.get("code") != 0:
        print(f"发送失败：{result['msg']}")
        return
    print("消息发送成功")

if __name__ == "__main__":
    main()

