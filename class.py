# # 마린 : 공격 유닛, 군인, 총을 쏠 수 있음

# name = "마린" # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체략 {0}, 공격력{1}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 포, 일반 모드/시즈 모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체략 {0}, 공격력{1}\n".format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)


class Unit:
    def __init__(self, name, hp, damage):
        # 멤버 변수
        self.name = name
        self.hp = hp
        self.damage = damage
        
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# 레이스 : 공중 유닛, 비행기, 클로킹
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 {1}".format(wraith1.name, wraith1.damage))  # 멤버변수를 외부에서 쓸때는 .을 활용하면 사용할 수 있다.

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True   # 클래스 외부에서 다른 변수를 할당 할수있음.

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))