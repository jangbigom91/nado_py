# 상속

# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        # 멤버 변수
        self.name = name
        self.hp = hp

# 공격 유닛 -> 일반 유닛을 상속받음
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # 상속
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage

        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))

        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 메딕 : 의무병, damage 없음


# 파이어뱃 유닛 만들기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격을 2번 받는다고 가정 -> 파괴
firebat1.damaged(25)
firebat1.damaged(25)
        