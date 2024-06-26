# 경로와 확장자 이용해 파일 찾고, 내용 읽기

import os

def searchFile(dirname, extention):
    filenames = os.listdir(dirname)
    for filename in filenames:
        filepath = os.path.join(dirname, filename)
        if os.path.isdir(filepath):
            searchFile(filepath, extention)
        elif os.path.isfile(filepath):
            name, ext = os.path.splitext(filepath)
            if ext == extention:
                with open(filepath, "r", encoding="utf-8") as f:
                    print(f.read())

searchFile("/Users/a-podo/Desktop/OS", '.js')