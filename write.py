import re

write_context = []  # まとめて書き込み用のリスト
css_write_context = []  # CSS用

# 読み込むファイルの指定
txt_file = "context.txt"
html_file = "web_test.html"
css_file = "write.css"

num = 1  


# context.txtの読み込み
def txt_read(txt_file, html_file):
    with open(txt_file, "r", encoding="utf-8") as file:
        lines = file.readlines() 

        for line in lines:
            line = line.strip()
            if "<1>" in line:
                if "<t>" in line:
                    size_1_wt_write(line, "bold")
                else:
                    size_1_wt_write(line, "normal")
            elif "<2>" in line:
                if "<t>" in line:
                    size_2_wt_write(line, "bold")
                else:
                    size_2_wt_write(line, "normal")
            elif "<3>" in line:
                if "<t>" in line:
                    size_3_wt_write(line, "bold")
                else:
                    size_3_wt_write(line, "normal")
            elif "<4>" in line:
                if "<t>" in line:
                    size_4_wt_write(line, "bold")
                else:
                    size_4_wt_write(line, "normal")
            else:
                print("~ THE END ~")


def size_1_wt_write(txt_contents, Thick):
    global num  # numをグローバル変数として参照
    size_1_txt_contents = re.findall(r"<1>(.*?)</1>", txt_contents)
    write_context.append(f"    <div id='len{num}'>\n        <p>" + "</p><p>".join(size_1_txt_contents) + "</p>\n    </div>")
    css_write_context.append(f"#len{num} {{\n    font-weight: {Thick};\n}}")

    num += 1


def size_2_wt_write(txt_contents, Thick):
    global num
    size_2_txt_contents = re.findall(r"<2>(.*?)</2>", txt_contents)
    write_context.append(f"    <div id='len{num}'>\n        <p>" + "</p><p>".join(size_2_txt_contents) + "</p>\n    </div>")
    css_write_context.append(f"#len{num} {{\n    margin: 0 auto;\n    font-size: 25px;\n    color: black;\n    font-weight: {Thick};\n}}")

    num += 1


def size_3_wt_write(txt_contents, Thick):
    global num
    size_3_txt_contents = re.findall(r"<3>(.*?)</3>", txt_contents)
    write_context.append(f"    <div id='len{num}'>\n        <p>" + "</p><p>".join(size_3_txt_contents) + "</p>\n    </div>")
    css_write_context.append(f"#len{num} {{\n    margin: 0 auto;\n    font-size: 50px;\n    color: black;\n    font-weight: {Thick};\n}}")

    num += 1


def size_4_wt_write(txt_contents, Thick):
    global num
    size_4_txt_contents = re.findall(r"<4>(.*?)</4>", txt_contents)
    write_context.append(f"    <div id='len{num}'>\n        <p>" + "</p><p>".join(size_4_txt_contents) + "</p>\n    </div>")
    css_write_context.append(f"#len{num} {{\n    margin: 0 auto;\n    font-size: 75px;\n    color: black;\n    font-weight: {Thick};\n}}")

    num += 1



# =====↓メイン処理はここから↓=====
txt_read(txt_file, html_file)

if write_context:
    # 最初と最後に文字を追加
    write_context.insert(0, "<!DOCTYPE html>\n<head>\n    <link rel='stylesheet' href='write.css'>\n</head>\n<body>")
    write_context.append("</body>\n</html>")

    # HTMLファイルに書き込み
    with open(html_file, "w", encoding="utf-8") as wt:
        write_contents = "\n".join(write_context)
        wt.write(write_contents)
else:
    print("html Error XD")

# CSS書き込み
if css_write_context:
    with open(css_file, "w", encoding="utf-8") as wt:
        css_write_contents = "\n".join(css_write_context)
        wt.write(css_write_contents)
else:
    print("css Error XD")
