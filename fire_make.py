import os
from database_read import database_read


send_dic = database_read()

dic_len = int(len(send_dic))


for num in range(dic_len):

    # ファイルの作成↓
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, (send_dic[num - 1]) + '.html')

    try:
        with open(file_path, mode='x') as f:
            f.write("init")
            print("file make success ^^+")

    except FileExistsError:
        print("file already exists ^^;")
        pass

