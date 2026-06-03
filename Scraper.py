import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://tw.news.yahoo.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
# 同時抓取 Yahoo 最常見的幾種新聞標題 class
titles = soup.find_all("a", class_=["StoryTileContent__title", "StreamItemContent__title", "video-title"])


# 取得今天的日期作為檔名
today = datetime.now().strftime("%Y-%m-%d")
filename = f"news_{today}.txt"

# 把抓到的標題寫進文字檔裡
with open(filename, "w", encoding="utf-8") as f:
    f.write(f"--- Yahoo 焦點新聞 ({today}) ---\n")
    for index, title in enumerate(titles, 1):
        clean_title = title.text.strip()
        if len(clean_title) > 5:
            f.write(f"{index}. {clean_title}\n")

print(f"成功儲存檔案：{filename}")
