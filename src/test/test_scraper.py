from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    # 设置 Chrome 浏览器驱动
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # 访问目标网页
    driver.get("https://study.uestc.cn/toutiao/#/")

    try:
        # 等待特定元素加载完成
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='someClass']")) # 替换为页面上的实际元素
        )

        # 抓取数据
        # 例如：找到所有包含新闻标题的元素
        news_elements = driver.find_elements(By.XPATH, "//h2[@class='newsTitle']") # 替换为正确的 XPath

        for news in news_elements:
            print(news.text)  # 打印新闻标题

    finally:
        # 关闭浏览器
        driver.quit()

if __name__ == "__main__":
    main()
