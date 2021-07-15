class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()

# ex) 드랍쉽 생성
dropship = FlyableUnit()    # 두개 이상의 다중 상속을 받을 때 super()를 쓰게 되면 순서상의 맨 처음에 상속받은 클래스에 대해서만 호출이 된다.