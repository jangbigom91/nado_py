# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# randrange()
for waiting_no in range(5):  # 0, 1, 2, 3, 4
    print("대기번호 : {}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))

##### 한 줄로 끝내는 for문

# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
students = [1, 2, 3, 4, 5]
print(students)

students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)

# 학생 이름을 소문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.lower() for i in students]
print(students)