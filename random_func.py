from random import *

# print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
# print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
# print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
# print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
# print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10이하의 임의의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10이하의 임의의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10이하의 임의의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10이하의 임의의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10이하의 임의의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10이하의 임의의 값 생성

# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성

# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성

# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성

# Quiz) 당신은 최근 코딩 스터디 모임을 새로 만들었다
# 월 4회 스터디를 하는데 3번을 온라인으로 하고 1번은 오프라인으로 하기로 했다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성

# 조건1 : 랜덤으로 날짜를 뽑아야함
# 조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

#(출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.

from random import *
date = randint(4, 28) # 1~3일은 제외라서 4일부터 시작, 28일 이내로 정해야 되서 randint(4, 28) 생성
print('오프라인 스터디 모임 날짜는 매월 ' + str(date) + '일로 선정되었습니다.')
