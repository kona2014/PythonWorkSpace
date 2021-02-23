from typing import Counter


url = 'http://naver.com'
print(url)

index = url.index("n")
print(index)

url = url[index:]
print(url)

index = url.index(".")
print(index)

url = url[:index]
print(url)

print(url[:3] + str(len(url)) + str(url.count("e")) + "!")