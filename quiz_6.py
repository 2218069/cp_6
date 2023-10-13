class Bungeoppang:
    total = 0 # 총 판매금액을 추적하기 위한 클래스 속성

    def __init__(self, type, price):
        self.type = type
        self.price = price

    def sell(self):
        return f"{self.type} 을 {self.price} 원에 팔았습니다."

    def eat(self):
        return f"{self.type} 을 먹었습니다."


cream = 붕어빵("슈크림 붕어빵", "600")
red_bean = 붕어빵("팥 붕어빵", "500")

red_bean.eat()
cream.eat()

red_bean.sell()
red_bean.sell()
print(red_bean.total)

cream.sell()
cream.sell()
cream.sell()
print(cream.total)
