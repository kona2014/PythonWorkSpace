# Q1
# 홍길동 씨의 과목별 점수는 다음과 같다. 홍길동 씨의 평균 점수를 구해 보자.

# 과목	점수
# 국어	80
# 영어	75
# 수학	55

print("Q1 -----------------------------------------------------------")
score = {"국어":80, "영어":75, "수학":55}
print(score)
total = score.get("국어")
total = total + score.get("영어")
total = total + score.get("수학")
print("총점 : " + str(total))
avg = total / 3
print("평균 : " + str(avg))


# Q2
# 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에 대해 말해 보자.
print("Q2 -----------------------------------------------------------")

a = 13
b = a % 2
print("1이면 홀수, 0이면 짝수 : " + str(b))


# Q3
# 홍길동 씨의 주민등록번호는 881120-1068234이다. 홍길동 씨의 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.
# ※ 문자열 슬라이싱 기법을 사용해 보자.
print("Q3 -----------------------------------------------------------")

jumin = "881120-1068234"
print("주민등록번호 : ", jumin)
print("년월일(YYMMDD) : ", str(jumin[0:6]))
print("뒷자리 : ", str(jumin[7:]))

 

# Q4
# 주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 주민등록번호에서 성별을 나타내는 숫자를 출력해 보자.
# >>> pin = "881120-1068234"
# ※ 문자열 인덱싱을 사용해 보자.
print("Q4 -----------------------------------------------------------")
pin = "881120-1068234"
index = pin.index("-")
index += 1
print(pin[index:index+1])

# Q5
# 다음과 같은 문자열 a:b:c:d가 있다. 문자열의 replace 함수를 사용하여 a#b#c#d로 바꿔서 출력해 보자.
# >>> a = "a:b:c:d"
print("Q5 -----------------------------------------------------------")
a = "a:b:c:d"
b = a.replace(":","#")

print(a)
print(b)


# Q6
# [1, 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1]로 만들어 보자.
# ※ 리스트의 내장 함수를 사용해 보자.
print("Q6 -----------------------------------------------------------")
lst = [1, 3, 5, 4, 2]
lst.sort()
lst.reverse()
print(lst)


# Q7
# ['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해 보자.
# ※ 문자열의 join 함수를 사용하면 리스트를 문자열로 쉽게 만들 수 있다.
print("Q7 -----------------------------------------------------------")
lst = ['Life', 'is', 'too', 'short']
print(lst[0], lst[1], lst[2], lst[3])

print(lst)
joined = " ".join(lst)
print(joined)


# Q8
# (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해 보자.
# ※ 더하기(+)를 사용해 보자.
print("Q8 -----------------------------------------------------------")
tpl = (1,2,3)
print(tpl)
print (id(tpl))
tpl = tpl + (4,) # 꼭 쉼표를 넣어줘서 튜플값임을 알려줘야 한다.
print(tpl)
print (id(tpl))


# Q9
# 다음과 같은 딕셔너리 a가 있다.

# >>> a = dict()
# >>> a
# {}
# 다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명해 보자.
print("Q9 -----------------------------------------------------------")
a = dict()

a['name'] = 'python'
print(a)
a[('a',)] = 'python'
print(a)
a[250] = 'python'
print(a)
# a[[1]] = 'python'  # unhashable type: 'list'
# print(a)



# Q10
# 딕셔너리 a에서 'B'에 해당되는 값을 추출해 보자.
# >>> a = {'A':90, 'B':80, 'C':70}
# ※ 딕셔너리의 pop 함수를 사용해 보자.
print("Q10 ----------------------------------------------------------")
a = {'A':90, 'B':80, 'C':70}
print(a)
print(a.pop('B'))
print(a)
print(a.popitem())
print(a)



# Q11
# a 리스트에서 중복 숫자를 제거해 보자.

# >>> a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
# ※ 집합 자료형의 요솟값이 중복될 수 없다는 특징을 사용해 보자.

a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
print(a, type(a))
a = set(a)
print(a, type(a))














# Q12
# 파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다. 다음과 같이 a, b 변수를 선언한 후 a의 두 번째 요솟값을 변경하면 b 값은 어떻게 될까? 그리고 이런 결과가 오는 이유에 대해 설명해 보자.

# >>> a = b = [1, 2, 3]
# >>> a[1] = 4
# >>> print(b)
