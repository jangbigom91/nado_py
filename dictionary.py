# 딕셔너리 {}

cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(5))
print(cabinet.get(5, '사용가능'))
# print("hi")

print(3 in cabinet)   # True
print(5 in cabinet)   # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
cabinet["A-30"] = "김종국"
cabinet["B-20"] = "조새호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 모두 지우기
cabinet.clear()
print(cabinet)
