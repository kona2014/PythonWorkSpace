# 표준 체중을 구하는 프로그램


# * 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자(kg) : 키(m) x 키(m) x 22
# 여자(kg) : 키(m) x 키(m) x 21

# 조건1. : 표준 체중은 별도의 함수 내에서 계산.
#     * 함수명 : std_weight
#     * 전달값 : 키(height), 성별(gender)

# 조건2. : 표준 체중은 소수점 둘째자리까지 표시

# (출력예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다. 

def std_weight(height, gender):
    score = 0

    if gender == "M":
        score = 22
    else:
        score = 21

    weight = round(height / 100 * height / 100 * score, 2)

    return weight

weight = std_weight(180, 'M')
print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다. ".format(180, weight))
weight = std_weight(159, 'F')
print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다. ".format(159, weight))

