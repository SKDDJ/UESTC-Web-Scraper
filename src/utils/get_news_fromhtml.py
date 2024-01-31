import re
import csv

# TODO: 把csv文件中的空行全部删除，然后输入给OpenAI处理，下一步Prompt的操作，明天处理https://miracleplus.feishu.cn/wiki/space/7314640316362817538?ccm_open_type=lark_wiki_spaceLinkopen_tab_from=wiki_home
# 假设 'sections' 是你从网页中提取的所有<section>标签内容
# 这里的sections内容从本地文件get_content.output中导入

# 打开文件并读取内容，将整个文件内容作为单个字符串存储在列表中
with open('../outputs/sections_output.txt', 'r', encoding='utf-8') as file:
    sections = [file.read()]
# 'sections' 变量现在是一个列表，其中包含一个字符串元素，该字符串包含了文件的全部内容


# 如果文件中的每一行都是一个独立的<section>，则 'sections' 变量现在包含了所有这些部分
# 如果整个文件是一个连续的<section>，那么你可能需要稍微修改这段代码来适应文件的实际格式
# 匹配新闻文字的正则表达式
news_pattern = r'<section style="text-align: center;margin-bottom: 8px;">.*?</section>\s*<section style="margin-bottom: 0px;">(.*?)</section>'

# 提取新闻文字
news_texts = []
for section in sections:
    matches = re.findall(news_pattern, section, re.DOTALL)
    news_texts.extend([re.sub('<[^<]+?>', '', text).strip() for text in matches])  # 移除HTML标签并清理文本

# 指定CSV文件路径
csv_file_path = '../outputs/2023_news.csv'  # 替换为你的文件路径
    

# 将新闻写入CSV文件
with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["新闻序号", "新闻内容"])
    for i, news in enumerate(news_texts, start=1):
        writer.writerow([i, news])

print("新闻已保存到CSV文件中。")





