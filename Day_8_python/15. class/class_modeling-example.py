class Human():
    '''인간'''

def create_human(name, weigth):
    person = Human()
    person.name = name
    person.weigth = weigth
    return person

Human.create = create_human

person = Human.create("철수", 60.5)

def eat(person):
    person.weigth += 0.1
    print("{}가 먹어서 {}kg가 되었습니다.".format(person.name, person.weigth))

Human.eat = eat

def walk(person):
    person.weigth -= 0.1
    print("{}가 걸어서 {}kg가 되었습니다.".format(person.name, person.weigth))

Human.walk = walk

person.walk()
person.eat()
person.walk()

"""
내가 직접 짜본 class

class Human():
    '''사람'''

    def create_human(name, weigth):
        person = Human()
        person.name = name
        person.weigth = weigth
        return person

    def eat(person):
        person.weigth += 0.1
        print("{}가 먹어서 {}kg가 되었습니다.".format(person.name, person.weigth))

    def walk(person):
        person.weigth -= 0.1
        print("{}가 걸어서 {}kg가 되었습니다.".format(person.name, person.weigth))

person = Human.create_human("철수", 60.5)
print(Human.eat(person))
"""
