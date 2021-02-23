def open_account():
    print("새로운 계좌가 개설되었다.")

open_account()


def deposite(balance, money):
    if money == 0:
        print("입금할 금액이 없어요. 잔액은 {0} 원입니다.".format(balance))
        return balance
    else:
        print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
        return balance + money

balance = 0
print(balance)
balance2 = deposite(balance, 1000)
print(balance2)
balance3 = deposite(balance2, 0)
print(balance3)


def test2(): 
    return '는 학생입니다.'
    
print('홍길동', test2())


print("Profile - Multi Parameter ----------------------------------------")

def profile(name, age, *lang): # *lang 는 가변인자
    print("Name : {0}\tAge : {1}\t".format(name, age), end=" ")
    for cod in lang: # 가변인자에 들어온 값들에 대해 순차적으로 반복한다.
        print(cod, end=" ")
    print() #줄바꿈의 역할

profile("Kim", 42, "Java", "ABAP")
profile("Her", 25, "UI5", "ABAP", "Java", "Python")