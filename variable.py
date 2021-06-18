####### 변수 #######

# 애완동물 소개
animal = "강아지"
name = "뿌꾸"
age = 10
hobby = "산책"
is_adult = age >= 3

print('우리집 ' + animal + '의 이름은 ' + name + '에요')

print(name + '는 ' + str(age) + '살이며, ' + hobby + '을 아주 좋아해요')
# print(name , '는 ' , age , '살이며, ' , hobby , '을 아주 좋아해요')

# print(name + '는 어른일까요? ' + str(is_adult))
print(name , '는 어른일까요?' , is_adult) # str() 쓰지 않고  ,사용해서 print가능
