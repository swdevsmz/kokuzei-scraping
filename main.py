import requests
from bs4 import BeautifulSoup
import csv
# import hashlib
# import time
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# スクレイピング対象のURL
url = "https://www.nta.go.jp/law/tsutatsu/kobetsu/hyoka/zaisan.htm"

# # 前回のハッシュ値を保存する変数
# previous_hash = ""

# # メール送信設定
# smtp_server = "smtp.example.com"
# smtp_port = 587
# smtp_user = "your-email@example.com"
# smtp_password = "your-password"
# to_email = "recipient@example.com"

# while True:


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

# # ハッシュ値を計算
# current_hash = hashlib.md5(str(table).encode('utf-8')).hexdigest()

# # ハッシュ値が変わった場合、メールを送信
# if previous_hash != "" and previous_hash != current_hash:
#     msg = MIMEMultipart()
#     msg['From'] = smtp_user
#     msg['To'] = to_email
#     msg['Subject'] = "The table has been updated"
#     body = "The table at {} has been updated.".format(url)
#     msg.attach(MIMEText(body, 'plain'))

#     server = smtplib.SMTP(smtp_server, smtp_port)
#     server.starttls()
#     server.login(smtp_user, smtp_password)
#     text = msg.as_string()
#     server.sendmail(smtp_user, to_email, text)
#     server.quit()

# # 現在のハッシュ値を保存
# previous_hash = current_hash

    # # 1時間待機
    # time.sleep(3600)
