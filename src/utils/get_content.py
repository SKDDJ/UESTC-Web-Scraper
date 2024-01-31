import requests
import re
import pandas as pd
import logging

# 设置日志记录
logging.basicConfig(filename='../../logs/get_content_log.txt', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def extract_sections_from_url(url):
    """从给定的URL中提取<section>标签内容"""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            sections = re.findall(r'<section.*?</section>', response.text, re.DOTALL)
            return sections
        else:
            logging.warning(f'请求失败，URL: {url}, 状态码: {response.status_code}')
            return []
    except Exception as e:
        logging.error(f'提取过程中发生错误，URL: {url}, 错误: {e}')
        return []

def process_urls_from_csv(csv_path, output_path):
    """处理CSV文件中的所有URL，并将提取的内容保存到指定文件"""
    df = pd.read_csv(csv_path)
    all_sections = []

    for url in df['sourceUrl']:
        sections = extract_sections_from_url(url)
        all_sections.extend(sections)

    # 将提取的内容保存到文件
    with open(output_path, 'w', encoding='utf-8') as file:
        for section in all_sections:
            file.write(section + '\n')

# CSV文件路径和输出文件路径
csv_path = '../outputs/output_2023.csv'  # 替换为实际路径
output_path = '../outputs/sections_output.txt'  # 替换为你想保存<section>内容的文件路径

# 处理CSV中的URL
process_urls_from_csv(csv_path, output_path)



# import requests
# from bs4 import BeautifulSoup

# # 网址
# url = 'https://mp.weixin.qq.com/s?__biz=MzIyMzgxMTI0Ng==&mid=2247549520&idx=1&sn=59694205c5f2d25df4ccffc84d410e21&chksm=e81ac191df6d4887b61df93f3a4cd00fb06a26cd2418737e29649466f48cc21768efbed2f329#rd'

# # 发送请求
# response = requests.get(url)

# # 检查响应状态
# if response.status_code == 200:
#     # print("请求成功，继续进行内容分析")
#     # print("响应状态码：", response.status_code)
#     # print("响应内容编码：", response.encoding)
#     # print("响应内容：", response.text)
    
#     import re

#     # 使用正则表达式提取内容
#     # 例如，提取以 "<section" 开始，以 "</section>" 结束的所有内容
#     sections = re.findall(r'<section.*?</section>', response.text, re.DOTALL)

#     # 打印提取到的内容
#     for section in sections:
#         print(section)

    
    
    
#     # 使用 BeautifulSoup 解析 HTML
#     # soup = BeautifulSoup(response.content, 'html.parser')
#     # soup = BeautifulSoup(response.content, 'html5lib')
    
#     # 示例：提取并打印网页标题
#     # page_title = soup.title.text if soup.title else "未提取到标题"
#     # print("网页标题:", page_title)

#     # 根据需要提取更多内容...
#     # 例如，提取特定的标签、类或 ID 的内容

#     # 打印提取的信息或进行简单分析

# else:
#     print("请求失败，状态码：", response.status_code)
