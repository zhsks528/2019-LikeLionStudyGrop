class Human():
    '''사람'''

    def create_human(name, weigth): # 다음강의때..
        person = Human()
        person.name = name
        person.weigth = weigth
        return person

    def eat(self):
        self.weigth += 0.1
        print("{}가 먹어서 {}kg가 되었습니다.".format(self.name, self.weigth))

    def walk(self):
        self.weigth -= 0.1
        print("{}가 걸어서 {}kg가 되었습니다.".format(self.name, self.weigth))

    def speak(self, message):
        print(message)


person = Human.create_human("성민이", 60.5)

person.eat()

