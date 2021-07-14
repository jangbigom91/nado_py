### ★★★ 파일 입출력

### ★★★ 파일 작성
# score_file = open("score.txt", "w", encoding="utf-8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# print("코딩 : 100", file=score_file)

# score_file.close()

### ★★★ 작성된 파일에 새로운 내용 쓰고 덮어쓰기
# score_file = open("score.txt", "a", encoding="utf-8") # "a" -> append, 파일이 있는곳에 내용을 추가
# score_file.write("과학 : 80") # write를 사용할 때는 줄바꿈을 따로 지정해줘야 한다.
# score_file.write("\n사회 : 80")

### ★★★ 파일 전체 읽어오기
# score_file = open("score.txt", "r", encoding="utf-8") # "r" -> read
# print(score_file.read()) # 파일 전체 다 읽어오기

# score_file.close()

### ★★★ 파일 한줄만 읽어오기
# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())

# score_file.close()

# ★★★ 파일의 내용이 몇줄인지 모를 떄 읽어오는 방법(반복문을 통해서 읽어올 수 있음.)
# score_file = open("score.txt", "r", encoding="utf-8")

# while True:
#     line = score_file.readline()
    
#     if not line:
#         break
#     print(line)

# score_file.close()


### ★★★ 리스트에 값을 다 넣어서 읽어오는 방법
score_file = open("score.txt", "r", encoding="utf-8")
lines = score_file.readlines() # list 형태로 저장

for line in lines:
    print(line, end="")

score_file.close()
