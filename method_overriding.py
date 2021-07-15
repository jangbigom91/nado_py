# 메소드 오버라이딩 : 상속의 개념 중 하나, 자식클래스가 자신의 부모클래스들 중 하나에 의해 이미 제공된 메소드를 특정한 형태로 구현
#                    클래스를 만들다 보면 메소드의 이름은 같지만 기능을 다르게 해야 할때가 있는데 이 때 메소드 오버라이딩 개념을 활용


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

# 드랍쉽 : 공중유닛, 수송기

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

# 벌처 : 지상유닛
vulture = AttackUnit("벌처", 80, 10, 20)

# 배틀크루저 : 공중유닛
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# 지상유닛일 경우에는 move함수, 공중유닛일 경우에는 fly함수로 호출해야 하는 불편함 -> 메소드 오버라이딩을 통해서 FlyableAttackUnit클래스에 move라는 함수를
# 만들어 줌으로써 지상유닛, 공중유닛 두 경우 모두 move라는 함수로 호출이 가능

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")
