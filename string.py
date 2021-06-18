####### 문자열 #######
sentence = '나는 소년입니다.'
print(sentence)

sentence2 = '파이썬은 쉬워요'
print(sentence2)

sentence3 = """
나는 소년이고, 
파이썬은 쉬워요
"""
print(sentence3)

####### 슬라이싱 #######
jumin = '990120-1234567'

print('성별 : ' + jumin[7])
print('연 : ' + jumin[0:2]) # 0부터 2 직전까지 (0, 1)
print('월 : ' + jumin[2:4]) # 2부터 4 직전까지 (2, 3)
print('일 : ' + jumin[4:6]) # 4부터 6 직전까지 (4, 5)

print('생년월일 : ' + jumin[:6]) # 처음부터 6 직전까지
print('뒤 7자리 : ' +jumin[7:]) # 7 부터 끝까지
print('뒤 7자리 (뒤에부터) : ' + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지

####### 문자열 처리 함수 #######
python = 'Python is Amazing'

print(python.lower()) # 소문자
print(python.upper()) # 대문자
print(python[0].isupper()) # True
print(len(python)) # 문자열의 길이
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)

index = python.index('n', index + 1)
print(index)

print(python.find("n"))

print(python.count("n"))

####### 문자열 포맷 #######
# print("a" + "b")
# print("a", "b")

# 방법 1
print("나는 %d살입니다." % 20) #d - 정수출력
print("나는 %s을 좋아해요" % "파이썬") # %s - 문자열 출력
print("Apple은 %c로 시작해요." % "A") # %c - 하나의 문자출력
print("나는 %s색과 %s색을 좋아해요" % ('파란', '빨간'))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "노랑"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "노랑"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "노랑"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color='빨강'))

# 방법 4 (v.3.6 이상~)
age = 20
color = '빨강'
print(f"나는 {age}살이며, {color}색을 좋아해요.")

####### 탈출문자 #######
# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

# 저는 '나도코딩'입니다.
print('저는 "나도코딩" 입니다.') # 문자열에 '', "" 표시는 하나씩 써야된다.
# print("저는 "나도코딩" 입니다.") # 오류

# \\ : 문장 내에서 \
print("C:\\Users\\ad\\Desktop\\py_workspace")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : 백스페이스 (한글자 삭제)
print("Redd\bApple") # \b 뒤에 있는 d 하나 삭제

# \t : 탭
print("Red\tApple")
