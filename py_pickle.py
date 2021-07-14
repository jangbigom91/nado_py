# 피클 -> 프로그램 상에서 사용하고 있는 데이터를 파일형태로 저장해주는 것
# 피클을 사용할때는 py명을 pickle.py로 하면 오류가 난다(pickle이 import가 안될수 있음)

import pickle

### 피클 파일 저장하기(쓰기)
profile_file = open("profile.pickle", "wb") # "wb"-> write binary 타입, 피클을 쓸때는 항상 "wb"를 지정해줘야 한다.
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}

print(profile)

pickle.dump(profile, profile_file) # profile에 있는 정보를 profile_file에 저장

profile_file.close()


### 피클파일에 있는 정보 가져오기(읽어오기)
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # profile_file에 있는 정보를 profile에 불러오기

print(profile)

profile_file.close()