import sqlite3
import os

date = input("date \n:")
title = input("title \n:")
context = input("context \n:")

# 現在位置の取得
current_dir = os.path.dirname(__file__)

db_path = os.path.join(current_dir, 'database.db')
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# date title context の 書き込み
cur.execute('INSERT INTO information(date, title, context) VALUES (?, ?, ?)', 
            (date, title, context))

conn.commit()

cur.close()
conn.close()