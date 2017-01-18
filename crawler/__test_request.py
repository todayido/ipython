import requests
from datetime import datetime
from bs4 import BeautifulSoup
res = requests.get("http://news.ifeng.com/o/dynpage/48-/1/plist.shtml")
res.encoding = "utf-8"
soup = BeautifulSoup(res.text, "html.parser")
header = soup.select("h2")
time = soup.select(".comListBox")
# print(soup.text)
# print(header)
# print("=========\n",  header[0])

item = soup.select("h2 a")
href = soup.select("h2 a[href]")
print(href)
i = 0
for it in item:
    print(item[i],it.text)
    i = i + 1
    # print(i.text)
