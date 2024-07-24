import requests
from bs4 import BeautifulSoup
import csv

# TODO 前回データの取得

# スクレイピング対象のURL
url = "https://www.nta.go.jp/law/tsutatsu/kobetsu/hyoka/zaisan.htm"
# ウェブページを取得
response = requests.get(url)
# レスポンスの内容を適切な文字コードでデコード
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text, 'html.parser')

# 表を取得
table = soup.find("table")

# 表のヘッダーを取得
headers = [header.text for header in table.find_all("th")]

# 表のデータを取得
rows = []
for row in table.find_all("tr"):
    rows.append([cell.text for cell in row.find_all("td")])

# CSVファイルに出力
with open("table.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

# TODO 前回データとの比較

# TODO 差分があれば差分を通知