import sqlite3
import os

def database_read():
    send_dic = []

    # 現在位置の取得
    current_dir = os.path.dirname(__file__)
    db_path = os.path.join(current_dir, 'database.db')


    # データベース接続
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()


    # データ取得
    cur.execute("SELECT * FROM information")

    rows = cur.fetchall()

    # 結果を表示
    for row in rows:
        send_dic.append(row[1])

    # print (send_dic)

    cur.close()
    conn.close()

    return(send_dic)