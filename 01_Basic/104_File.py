score_file = open("105_File_test.txt", "w", encoding="utf8") # 'w' 옵션은 오버라이트, 지우고 새로 쓴다.
print("수학 : 100", file=score_file)
print("영어 : 50",  file=score_file)
score_file.close()

score_file = open("105_File_test.txt", "a", encoding="utf8") # 'a' - Append"
print("물리 : 100", file=score_file)
print("화학 : 50",  file=score_file)
score_file.close()

# score_file = open("105_File_test.txt", "w", encoding="utf8")
# score_file.write("수학 : 70")
# score_file.write("영어 : 100") # 그냥 쓰면 줄 안바뀜. 
# score_file.close()


# score_file = open("105_File_test.txt", "a", encoding="utf8")
# score_file.write("수학 : 70")
# score_file.write("\n영어 : 100") # 줄바꿈
# score_file.close()


# score_file = open("105_File_test.txt", "r", encoding="utf8") # 읽기 
# print(score_file.read())
# score_file.close()


score_file = open("105_File_test.txt", "r", encoding="utf8") # 읽기 
while True:
    line = score_file.readline()    #  한 줄 읽기.
    if not line:
        break
    else:
        print(line, end="")

score_file.close()
