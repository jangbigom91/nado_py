# super() : 자식클래스에서 부모클래스의 내용을 사용하고 싶은 경우
#         : super().부모클래스내용
#         : 두 개 이상의 다중 상속을 받을 때 super()를 쓰게 되면 순서상의 맨 처음에 상속받은 클래스에 대해서만 호출이 된다.(뒤에 상속받은 클래스는 호출이 안된다.)
#         : 두 개 이상의 다중 상속을 받을 때는 상속받은 클래스.__init__(self)를 활용하는 게 좋다.


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
        # Unit.__init__(self, name, hp, 0)  # Unit을 통해서 __init__하는 경우
        super().__init__(name, hp, 0)       # super()를 통해서 __init__하는 경우 -> self없이 사용해야 한다.
        self.location = location


