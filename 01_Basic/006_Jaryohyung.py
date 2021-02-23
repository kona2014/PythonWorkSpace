myset = {1,2,3,3,3,3}
print(myset)

myset2 = {1,2,4}

print(myset & myset2) # 교집합
print(myset | myset2) # 합집합
print(myset.intersection(myset2)) # 교집합
print(myset.union(myset2))  # 합집합
print(myset - myset2) # 차집합
print(myset.difference(myset2)) # 차집합


myset2.add(7) # 추가
print(myset2)

myset2.remove(2) #제거
print(myset2)

# 자료구조의 변경
myset_1 = {1,2,3,3,3,3}
print(myset_1, type(myset_1))

myset_1 = list(myset_1)
print(myset_1, type(myset_1))

myset_1 = tuple(myset_1)
print(myset_1, type(myset_1))

myset_1 = set(myset_1)
print(myset_1, type(myset_1))


# 랜덤으로 리스트에서 당첨자 뽑기
from random import *

lst = range(1,21)
print(lst, type(lst))
lst = list(lst)
print(lst, type(lst))
shuffle(lst)
print(lst, type(lst))

winner = sample(lst,1)
print("Winner : " + str(winner) )

lst = set(lst)
print(lst, type(lst))
lst.remove(winner[0])
print(lst, type(lst))

lst = list(lst)
print(lst, type(lst))
print("2nd : " + str(sample(lst,3)))
