# 패스 : 아무것도 안하고 일단은 넘어간다는 의미

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        # 멤버 변수
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# 공격 유닛 -> 일반 유닛을 상속받음
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed) # 상속
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage

        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))

        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):  # 다중상속을 받을떄는 ,로 구분하면 된다.
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상스피드는 0으로 처리
        Flyable.__init__(self, flying_speed)   

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# 건물
class BuildingUnit(Unit): # Unit을 상속 받음
    def __init__(self, name, hp, location):
        pass  # 아무것도 안하고 일단은 넘어간다는 의미


# ex) 서플라이 디폿을 건설한다고 가정
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")


# pass 사용 예시
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over() # game_over는 pass가 있어서 아무것도 없이 그냥 넘어간다.