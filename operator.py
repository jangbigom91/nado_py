####### 연산자 #######
print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2

print(2**3) # 2^3 = 8
print(5%3) # 나머지 구하기 2
print(10//3) # 몫구하기 3

print(10 > 3) # True
print(4 >= 7) # False
print(3 == 3) # True

print(3 != 3) # False
print(not(1 != 3)) # False

print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True

print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True

print(5 > 4 > 3) # True
print(5 > 4 > 7) # False

####### 간단한 수식 #######
print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20

number = 2 + 3 * 4
print(number) # 14

number = number + 2
print(number) # 16

number += 2
print(number) # 18

number *= 2
print(number) # 36

number /= 2
print(number) # 18

number %= 2
print(number) # 0

####### 숫자 처리 함수 #######
print(abs(-5)) # 절대값
print(pow(4, 2)) # 4**2 - 16
print(max(5, 12)) # 최대값
print(min(5, 12)) # 최소값
print(round(3.14)) # 반올림

from math import *
print(floor(4.99)) # 내림
print(ceil(3.14)) # 올림
print(sqrt(16)) # 제곱근
