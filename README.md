# UESTC-Web-Scraper

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 代码逻辑

### `main.py` 获取所有URL链接

  得到 `final_output.csv` ， 表格信息如下：

| Column     | Non-Null Count | Dtype  |
| ---------- | -------------- | ------ |
| Unnamed: 0 | 10460 non-null | int64  |
| id         | 10460 non-null | object |
| title      | 10460 non-null | object |
| sourceUrl  | 10460 non-null | object |
| addTime    | 10460 non-null | object |

  **表格head**

| id | title                            | sourceUrl                                                      | addTime                                                                                                                                                                                              |
| -- | -------------------------------- | -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0  | 1ece0433b77344ec97afa695338b4195 | 布里斯托大学3+1本硕连读项目分享会“学长学姐对你说”活动通知    | [Link](http://mp.weixin.qq.com/s?__biz=MzA3NjgxNzYzNw==&mid=2682768942&idx=1&sn=121d10ba612131749900b10271d92ef9&chksm=85481ba4b23f92b26dee03c2106de4ed8200c2e9a61c394210a516c480e1f25fdcbb669d9ce9#rd) |
| 1  | c70747dd9b904119afe39514a3a97909 | 来了，成电早新闻（2024.01.22）                                 | [Link](http://mp.weixin.qq.com/s?__biz=MzIyMzgxMTI0Ng==&mid=2247549249&idx=1&sn=8d33ee66ad8a103067922bbf969b23fa&chksm=e81ac280df6d4b968aa8d9eff18a6dbd5cc3962433a265d6a4103a5fdd9dc9beb556d267f7e6#rd) |
| 2  | e530704bdc784de1b314dd58ce9cd427 | 电子科大机关党委举行2023年度党支部书记抓党建工作述职评议考核会 | [Link](http://mp.weixin.qq.com/s?__biz=MzIyMzgxMTI0Ng==&mid=2247549249&idx=2&sn=100f13d09898f1f87c439c39c1663310&chksm=e81ac280df6d4b96cf5281be4a123ed618ce5f4d04a50e592060cf807d0a61eb06e0a32d1c13#rd) |
| 3  | 8d8f5262dc02442f89dd097ad2b0d078 | 学校举行第六届“平安成电卫士”表彰大会                         | [Link](https://news.uestc.edu.cn/?n=UestcNews.Front.DocumentV2.ArticlePage&Id=91448)                                                                                                                    |
| 4  | b5b5f92a5d1a402ba3c371a1784b240c | 学校召开2024年教职工因公出国（境）工作小组会议                 | [Link](https://news.uestc.edu.cn/?n=UestcNews.Front.DocumentV2.ArticlePage&Id=91439)                                                                                                                    |
| 5  | 79a2176d3f5b43d9bd42c577eb0d7591 | 走进华严洞窟数字化（二）｜华严洞浮雕3D打印                     | [Link](http://mp.weixin.qq.com/s?__biz=MzA4MTQ5MzgyOA==&mid=2654399382&idx=1&sn=0ed36d77ea5f967d7be643649723f73e&chksm=845661bdb321e8ab3cde172a7c726acfd9553d3d95d44ed6897c815886582090c17c63b32649#rd) |

需要从中得到“来了，成电早新闻”的URL再进一步处理

### `extract_yearnews2csv.py`提取指定年份的所有早新闻转化为csv表格

例如运行 `src/utils/extract_yearnews2csv.py`，得到 `outputs/output_2023.csv`
年份在 `extract_yearnews2csv.py`中修改

| order | id                               | title                         | sourceUrl                                                                                                                                                                                            | addTime             |
| ----- | -------------------------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| 161   | 145b924d08904d6a9bd0c7059ba5f36d | 来了，成电早新闻（2023.12.31) | [Link](http://mp.weixin.qq.com/s?__biz=MzIyMzgxMTI0Ng==&mid=2247548455&idx=1&sn=242cf9cb45176e90b33c6f8272b7d8ea&chksm=e81afde6df6d74f06b8d1ecc20ea1e580055a11da535c4f7b370fc292bb5ecf7df2c40bd32c7#rd) | 2023-12-31T07:00:10 |
| 165   | c16f584ae3434d9c960608b2b1ea7087 | 来了，成电早新闻（2023.12.30) | [Link](http://mp.weixin.qq.com/s?__biz=MzIyMzgxMTI0Ng==&mid=2247548434&idx=1&sn=71592c5f601934d90d0fd61a590b4e32&chksm=e81afdd3df6d74c53fda547fca93cc0e017939fd2e79e3b3b9b264791f16f6bca13ff45a2201#rd) | 2023-12-30T07:00:10 |
| 174   | aeb9ddecec2e4cb7aa90a9808bb7e68a | 来了，成电早新闻（2023.12.29) | [Link](http://mp.weixin.qq.com/s?__biz=MzIyMzgxMTI0Ng==&mid=2247548383&idx=1&sn=d38585da2037e5c60601e43c70006f61&chksm=e81afe1edf6d77084ecec580ed0f05eb4780410d20fa8a77fc9ba6b3f3697e000c0cddd7e630#rd) | 2023-12-29T07:00:10 |
| 184   | 78cd1fc7a0ee478a8c1cbda4ac8120a6 | 来了，成电早新闻（2023.12.28) | [Link](http://mp.weixin.qq.com/s?__biz=MzIyMzgxMTI0Ng==&mid=2247548318&idx=1&sn=c94379ae6f1f822f76feeccb60e9d953&chksm=e81afe5fdf6d7749f2a37bc8ccd9c01ba9a8637ef7a7a62822f9500f7a268c14ea44a4a1688b#rd) | 2023-12-28T07:00:10 |
| 192   | 05096b6a32b14e6f9c8f9d24d9a4f891 | 来了，成电早新闻（2023.12.27) | [Link](http://mp.weixin.qq.com/s?__biz=MzIyMzgxMTI0Ng==&mid=2247548270&idx=1&sn=af8936fa70764f52f3f6d7ea3682526a&chksm=e81afeafdf6d77b904338705d2ba113f8837dddd10bec8b8e7a7f3986ff3891769a3274696d6#rd) | 2023-12-27T07:00:10 |
| 200   | baa929aa8c4140769111eb0931d42edb | 来了，成电早新闻（2023.12.26) | [Link](http://mp.weixin.qq.com/s?__biz=MzIyMzgxMTI0Ng==&mid=2247548219&idx=1&sn=2bcd8c775c436dc123cc38f8d700bd6c&chksm=e81afefadf6d77ececc503ddd9aceb56dd9f440f4f99d28ff6cccdbae05c326640bfd69ebbcb#rd) | 2023-12-26T07:00:10 |
| 213   | 8239e2500b464d31843c24be631ddbac | 来了，成电早新闻（2023.12.25) | [Link](http://mp.weixin.qq.com/s?__biz=MzIyMzgxMTI0Ng==&mid=2247548167&idx=1&sn=456685b42be9a33265f65a40f8503d43&chksm=e81afec6df6d77d093eef471288fb6137eb780e1c6be749d53a9ee7ee679b4cc2219deaa9765#rd) | 2023-12-25T07:00:10 |

### `get_content.py` 得到未清洗的新闻数据

运行 `src/utils/get_content.py`得到原始的HTML，存到 `src/outputs/sections_output.txt`文件中

### `get_news_fromhtml.py` 将HTML转化为csv

运行 `src/utils/get_news_fromhtml.py`，将 `src/outputs/sections_output.txt`文件处理为 `src/outputs/2023_news.csv`

| 新闻序号 | 新闻内容                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1        | 12月29日，光电学院召开教职工党支部年终交流会，各支部书记汇报一年来支部建设、续航项目推进等情况。                                                                                                                                                                                                                                                                                                               |
| 2        | 12月29日，国家管网集团联合管道有限责任公司西部分公司--电气自动化技术培训班结业典礼在自动化学院举办。学院党委书记张均强、副院长邱根，国家管网集团联合管道有限责任公司西部分公司主管工程师李佳富、授课导师代表、36名学员出席典礼。                                                                                                                                                                               |
| 3        | 12月28日，深圳高研院召开党委理论学习中心组（扩大）学习会，学习习近平总书记在纪念毛泽东同志诞辰130周年座谈会上的重要讲话精神、重要文章《加强基础研究 实现高水平科技自立自强》，并观看学习专题节目《榜样8》。                                                                                                                                                                                                    |
| 4        | 12月27日-28日，中国高等教育学会教育基金工作研究分会2023年学术年会在复旦大学召开，我校教育基金会负责人参加分会常务理事会议及圆桌论坛。                                                                                                                                                                                                                                                                          |
| 5        | 近日，学校“形势与政策”课面向全校本科生开设以“深刻把握教育、科技、人才在全面建设社会主义现代化国家中的地位作用”为主题的专题教学，校长曾勇，校领导朱宏、申小蓉、胡皓全、胡俊、孔令讲、罗光春登上讲台为同学们授课，引导大学生紧跟党和国家发展步伐，坚定不移听党话、跟党走，深刻领悟“两个确立”的决定性意义，进一步增强“四个意识”、坚定“四个自信”、做到“两个维护”，努力成为担当民族复兴大任的时代新人。 |
| 6        | ...                                                                                                                                                                                                                                                                                                                                                                                                            |

### 通过OpenAI API 利用LLM进行数据处理

基本逻辑：

* 将csv格式的新闻按照行来输入，通过Prompt engineering得到格式化输出
* 输出应该是csv表格

## TODO

- [ ] 所有的代码逻辑组合起来
- [ ] send email when script crash
- [ ] Update installation instructions
- [ ] Add code examples to the usage section
- [ ] Improve documentation for contributing guidelines
- [ ] Update contact information with my details

## Description

A brief description of the project.

## Table of Contents

- [UESTC-Web-Scraper](#uestc-web-scraper)
  - [代码逻辑](#代码逻辑)
    - [`main.py` 获取所有URL链接](#mainpy-获取所有url链接)
    - [`extract_yearnews2csv.py`提取指定年份的所有早新闻转化为csv表格](#extract_yearnews2csvpy提取指定年份的所有早新闻转化为csv表格)
    - [`get_content.py` 得到未清洗的新闻数据](#get_contentpy-得到未清洗的新闻数据)
    - [`get_news_fromhtml.py` 将HTML转化为csv](#get_news_fromhtmlpy-将html转化为csv)
    - [通过OpenAI API 利用LLM进行数据处理](#通过openai-api-利用llm进行数据处理)
  - [TODO](#todo)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

## Installation

Instructions on how to install and set up the project.

## Usage

Instructions on how to use the project and any relevant examples.

## Contributing

Guidelines for contributing to the project.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

- Author: Yiming Shi
- Email: yimingshi666@gmail.com
- GitHub: [My GitHub Profile](https://github.com/SKDDJ)
- Website: [My Website](https://academic.shiym.top)
