gun = 10

# # 전역변수를 파라미터로 받았지만 펑션 내부에서는 지역변수로 쓰이고 전역변수 값을 바꿀 수 없다. 
# def check_point(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# check_point(gun, 2)
# print("남은 총 : {0}".format(gun))


# 전역변수를 파라미터로 받고 Return 받으면 전역변수 값을 바꿀 수 있다. 
def check_point(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = check_point(gun, 2)
print("남은 총 : {0}".format(gun))