print("Python", "Java", "JavaScript", sep=" vs ", end="?") # 기본적으로 줄바꿈인데 end= 처리하면 줄바꿈 대신에 다른 값으로 대체되면서 줄이 안바뀐다.
print("무엇이 더 재밌을까 ?")


# import sys

# print("Python", file=sys.stdout)
# print("Python", file=sys.stderr)


# scores = {"수학":0, "영어":50, "코딩":100}

# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(30), sep=":")

# # 반올림 부분은 좀 더 공부해봐야함. 부동소숫점 어쩌고 하면서 ... 
# print(round(12345.55000,1))
# print(round(12345.55500,2))
# print(round(12345.55550,3))
# print(round(12345.55555,4))
# print(round(55555,-1))
# print(round(55550,-2))
# print(round(55500,-3))
# print(round(55000,-4))
# print(round(50000,-5))


# for num in range(1,21):
#     print(str(num).zfill(3))

# answer = input()  # 입력 받으면 문자열로 들어감. 
# print(answer, type(answer))  # 777 <class 'str'> 
# answer = 10       # 숫자로 들어감. 
# print(answer, type(answer))  # 10 <class 'int'>


# 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(555))
# 부호 표시
print("{0: >+10}".format(555))
print("{0: >+10}".format(-555))
print("{0:_>+10}".format(-555))  # 앞에 언더바
print("{0:A>+10}".format(-555))  # 앞에 채움
print("{0:_<+10}".format(-555))  # 뒤에 언더바

print("{0:>+30,}".format(-5559999))  # 세자리 마다 콤마 + 30자리 확보, 우측정렬, 부호 표시

print("{0:f}".format(5/3)) # 소숫자리 표시
print("{0:.3f}".format(5/3)) # 소숫자리 표시(뒤에 세자리 까지 반올림)