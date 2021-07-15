# with -> with를 사용해서 파일을 간편하게 읽어오고 쓸수 있음. 그리고 파일을 읽고 쓸 때 따로 close()를 지정해주지 않아도 with가 끝나면 자동으로 close 된다.

import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf-8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf-8") as study_file:
    print(study_file.read())