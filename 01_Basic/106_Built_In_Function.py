# input : 사용자 입력을 받는 함수

# language = input("무슨 언어를 좋아하세요?")
# print("{0}는 매우 훌륭한 언어입니다.".format(language))


# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random

# print(dir())
# import pickle

# print(dir())


# print(dir(random))


# lst = [1, 2, 3]
# print(dir(lst))

# import os
# print(os.getcwd())

# import glob
# print(glob.glob("*.py"))

# folder = "sample_dir"
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제했다.")
# else:
#     os.makedirs(folder)
#     print(folder, "폴더를 생성했다.")

# import os
# print(os.listdir())

import time

print(time.localtime())
print(time.strftime("%Y/%m/%d %H:%M:%S")) # m 이랑 d 는 소문자로 써야한다. 

import datetime
print("오늘 날짜는 ", datetime.date.today())

today = datetime.date.today()
td = datetime.timedelta(days=100)
print(today + td)

