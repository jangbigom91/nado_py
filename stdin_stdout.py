# 표준 입출력
# print("Python", "Java")
print("Python", "Java", sep=",")
print("Python", "Java", "JavaScript", sep=" vs ")
print("Python", "Java", "JavaScript", sep=" vs ", end="?")

import sys
# sys.stdin   - 입력 버퍼, 입력 버퍼가 없으면 키보드 입력
# sys.stdout  - 출력 버퍼, 출력 버퍼가 지정되어 있지 않으면 터미널 출력  (표준 출력)
# sys.stderr  - 출력 버퍼, 출력 버퍼가 지정되어 있지 않으면 터미널 출력 (에러 출력)

print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)


# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=" : ") # ljust : 왼쪽 정렬(뒤에 숫자만큼 자리확보), rjuct : 오른쪽 정렬(뒤에 숫자만큼 자리확보)


# 은행 대기순번표
# 출력 ex) 001, 002, 003...

for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3)) # zfill() -> 뒤에 있는 숫자만큼 공간을 확보하고, 빈 공간은 0으로 채우는 메서드


answer = input("아무 값이나 입력하세요 : ")  # input 형태로 값을 받게 되면 항상 값의 타입은 문자열(str) 형태로 값을 받는다.
print("입력하신 값은 " + answer + " 입니다.")