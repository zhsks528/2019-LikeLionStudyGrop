class Car():
    
    def run(self):
        print("차가 달립니다.")


class Truck(Car):
    
    def load(self):
        print("짐을 실었습니다.")
    # 이 아래에서 run 메소드를 오버라이드 하세요.
    def run(self):
        print("트럭이 달립니다.")
    
truck = Truck()
truck.run()
