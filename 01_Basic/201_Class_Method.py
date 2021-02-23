#  Super Class 초기화 할 때 suoer 쓰면 다중상속 시 맨처음 super 만 초기화 된다. 

class Unit:
    def __init__(self):
        print("Unit Constructor")

class Flyable:
    def __init__(self):
        print("Flyable Constructor")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # super().__init__()  # 맨 처음에 상속받는 클래스에 대해 init 처리된다. 
        Flyable.__init__(self)
        Unit.__init__(self)


dropship = FlyableUnit()
        
