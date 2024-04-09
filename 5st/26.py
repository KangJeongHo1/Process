# os 파일 시스템 명령 함수

import os

pwd = "/Users/a-podo/Desktop/OS"

# 디렉터리 내부 리스트 업
filename = os.listdir(pwd)
print(filename)

# 디렉터리인지 아닌지 여부
print(os.path.isdir(filename[0]))
print(os.path.isdir(pwd + '/anony'))

# 파일인지 아닌지 여부
print(os.path.isfile(filename[0]))
print(os.path.isfile(pwd + '/anony'))

# 파일이름과 확장자 분리
filepath = pwd + '/' + filename[0]
print(filepath)
name, ext = os.path.splitext(filepath)
print(name)
print(ext)