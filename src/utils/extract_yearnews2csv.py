import pandas as pd
import re

def extract_news_by_year(csv_path, year, output_csv_path):
    # 读取CSV文件
    df = pd.read_csv(csv_path, encoding='utf-8')

    # 正则表达式匹配标题
    pattern = f"来了，成电早新闻（{year}.\d+.\d+"

    # 过滤出匹配的行
    filtered_df = df[df['title'].str.contains(pattern)]

    # 保存到新的CSV文件
    filtered_df.to_csv(output_csv_path, index=False, encoding='utf-8')

    return filtered_df

# 使用函数
csv_path = "../outputs/final_output.csv"  # 替换为原始CSV文件路径
output_csv_path = "../outputs/output_2023.csv"  # 替换为想保存的新CSV文件路径

# 提取2023年的数据
extracted_df = extract_news_by_year(csv_path, 2023, output_csv_path)
print(extracted_df.head())
