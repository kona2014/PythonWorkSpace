
# 리스트
subway = [10, 20, 30]

print(subway.index(20))

subway.append(99)

print(subway)

subway.insert(subway.index(30), 44)
print(subway)


print(subway.pop())
print(subway)

subway.sort()
print(subway)

subway.reverse()
print(subway)

subway.clear()
print(subway)


#  사전 - Key : Value 형태.
cabinet = {1:'aa', 3:'bb'}
print(cabinet.get(1))

print(1 in cabinet)
print(2 in cabinet)
print(3 in cabinet)

# del cabinet[3]
# print(cabinet)

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

cabinet.clear()
print(cabinet)




