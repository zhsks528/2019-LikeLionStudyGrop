class Human():

    def __init__(self, name, weigth):
        '''초기화 함수'''
        self.name = name
        self.weigth = weigth

    def __str__(self):
        '''문자열화 함수'''
        return "{}(몸무게 {}kg)".format(self.name, self.weigth)

    def eat(self):
        person.weight += 0.1
        print("{}가 먹어서 {}kg가 되었습니다.".format(self.name, self.weight))

    def walk(self):
        person.weight -= 0.1 
        print("{}가 걸어어서 {}kg가 되었습니다.".format(self.name, self.weight))

person = Human("성민", 60.5)
print(person)
