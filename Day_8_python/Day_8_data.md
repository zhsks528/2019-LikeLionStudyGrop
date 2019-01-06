## 멋사 스터디 8일차

15. 클래스와 객체지향 프로그래밍

16. 상속과 다형성

17. Comprhension

18. 날짜와 시간



## 15. 클래스와 객체지향 프로그래밍

### 15.1 자료형 다루기

#### 자료형

- `type( a ) # type( 변수명 )` : 자료형
- `isinstance( 42, int ) # isinstance( 값, 자료형 )` : 자료형 검사



### 15.2 인스턴스 이해

#### 15.2.1 클래스

- 함수나 변수들을 모아 놓은 집합체

#### 15.2.2 인스턴스

- 클래스에 의해 생성된 객체
- 인스턴스 각자 자신의 값을 가지고 있다.



### 15.3 클래스 만들기

#### 15.3.1 클래스 선언

```
class Human( ):
    '''사람'''
```

#### 15.3.2 인스턴스 생성

```
person1 = Human( )
person2 = Human( )
```

- 클래스와 인스턴스를 이용하면 데이터와 코드를 사람이 이해하기 쉽게 포장할 수 있다.



### 15.4 모델링

#### 모델링(modeling)

- 클래스로 현실의 개념을 표현하는 것



### 15.5 메소드 이해하기

#### 15.5.1 메소드(Method)

- 메소드는 함수와 비슷하다.
- 클래스에 묶여서 클래스의 인스턴스와 관계되는 일을 하는 함수



#### 클래스 내부에 함수를 포함시킨 예

```
class Human( ):
    '''인간'''
    def create( name, weight ): # 다음 강의에서 자세히 설명
        person = Human()
        person.name = name
        person.weight = weight
        return person

    def eat( self ):
        self.weight += 0.1
        print("{}가 먹어서 {}kg이 되었습니다".format(self.name, self.weight))

    def walk( self ):
        self.weight -= 0.1
        print("{}가 걸어서 {}kg이 되었습니다".format(self.name, self.weight))

person = Human.create("철수", 60.5)
person.eat()
```



#### 15.5.2 self

- **메소드의 첫번째 인자**
- 인스턴스의 매개변수를 전달 할 때는 self 매개변수는 생략하고 전달



### 15.6 특수한 메소드

#### 15.6.1 초기화 함수

- `__init__` : 인스턴스를 만들 때 실행되는 함수

#### 15.6.2 문자열화 함수

- `__str__` : 인스턴스 자체를 출력 할 때의 형식을 지정해주는 함수

```
class Human( ):
    '''인간'''
    def __init__( self, name, weight ):
        '''초기화 함수'''
        self.name = name
        self.weight = weight

    def __str__( self )
        '''문자열화 함수
        return "{} ( 몸무게 {}kg )".format( self.name, self.weight )

person = Human( "사람", 60.5 ) # 초기화 함수 사용
print( person ) # 문자열화 함수 사용
```



## 16. 상속과 다형성

### 16.1 상속

#### 상속(Inheritance)

- 상속하는 클래스를 부모 클래스
- 상속받는 클래스를 자식 클래스
- 자식 클래스가 부모 클래스의 내용을 가져다 쓸 수 있는 것

```
class Animal( ):
    def walk( self ):
        print( "걷는다" )

    def eat( self ):
        print( "먹는다" )

class Human( Animal ):
    def wave( self ):
        print( "손을 흔든다" )

class Dog( Animal ):
    def wag( self ):
        print( "꼬리를 흔든다" )
```

![inheritance](https://user-images.githubusercontent.com/38130934/50733001-74125280-11c8-11e9-9726-5c8388494139.PNG)



### 16.2 단순 오버라이드

#### 오버라이드(Override)

- 같은 이름을 가진 메소드를 덮어 쓴다는 의미

```
class Animal( ):
    def greet( self ):
        print( "인사한다" )

class Human( Animal ):
    def greet( self ):
        print( "손을 흔든다" )

class Dog( Animal ):
    def greet( self ):
        print( "꼬리를 흔든다" )
```

![override](https://user-images.githubusercontent.com/38130934/50733131-eb48e600-11ca-11e9-96fc-c7f66192fd4c.PNG)



### 16.3 super()

#### super()

- 자식클래스에서 부모클래스의 내용을 사용하고 싶은 경우
- super().부모클래스내용

```
class Animal( ):
    def __init__( self, name ):
        self.name = name

class Human( Animal ):
    def __init__( self, name, hand ):
        super().__init__( name ) # 부모클래스의 __init__ 메소드 호출
        self.hand = hand

person = Human( "사람", "오른손" )
```



### 16.4 내 예외 만들기

#### 예외 정의

- 사용자가 직접 예외처리를 하면 코드의 직관성을 높일 수 있다.
- 파일을 하나 만들어 예외를 정의
- Exception 클래스를 상속받아 만든다

```
try:
    sign_up( )
except BadUserName:
    print( "이름으로 사용할 수 없는 입력" )
except PasswordNotMatched:
    print( "입력한 패스워드 불일치")
```



## 17. Comprhension

### 17.1 List comprehension

- 파이썬의 유용한 도구
  - 예1 `[ i*i for i in range(1,11) ] # [ 계산식 for문 ]`
  - 예2 `[ i*i for i in range(1,11) if i % 2 == 0 ] # [ 계산식 for문 조건문 ]`
  - 예3 `[ ( x, y ) for x in range(15) for y in range(15) ] # [ 계산식 for문 for문 ]`

### 17.2 Dictionary comprehension

- 파이썬의 유용한 도구
- 예시
  - `{ "{}번".format(number):name for number, name in enumerate(students) } # [ 형식 for문 ]`
  - `{student:score for student, score in zip(students, scores)}`



## 18. 날짜와 시간

### 18.1 datatime

#### datetime 모듈

- 날짜와 시간을 사용하게 해주는 라이브러리

```
>>> import datetime
```

- 시간 설정

  datetime.datetime(년도, 월, 일, 시간, 분, 초)

- 현재시간 알아보기

  datetime.datetime.now()



### 18.2 timedelta

#### timedelta 클래스

- 시간의 연산을 가능하게 해주는 클래스