## 멋사 스터디 6일차

6. 리스트
7. for 반복문
8. 모듈
9. 활용하기
10. 딕셔너리와 튜플

## 6. 리스트

### 6-1 리스트 사용

#### List

- 여러개의 값을 담을 수 있는 변수

  ```
  list1 = [1,2,3,4,5]
  ```

- 값 읽어오기

  - 리스트를 사용할때는 0번째가 첫번째
  - 첫번째 값 `list1[0]`
  - 두번째 값 `list1[1]`
  - 뒤에서 첫번째 값 `list1[-1]`
  - 뒤에서 두번째 값 `list1[-2]`
  - 리스트에 들어있는 값 보다 큰 값을 읽어오려고 하면 에러
    - 예. 위의 list1에서 `list1[5]` 또는 `list1[-6]`은 에러

- 값 쓰기

  - 변수와 같이 `list1[0]=10`이라고 하면 list의 첫번째 값이 10으로 변경



### 6-2 리스트 수정

#### 리스트에 새로운 값을 추가하는 방법

- `list1=[1,2,3]`이라고 할 때
- append를 이용
  - `list1.append(4)`
  - append를 이용하면 리스트에 새로운 값이 추가된다.
- 뒤에 새로운 리스트를 더하기
  - `list2=list1+[4]`
  - list1은 그대로 두고, 새로운 리스트를 만들어 낸다.

#### 리스트에 값이 들어있는지 확인하는 방법

- in 연산을 이용

  ```
  #12라는 값이 리스트에 들어있는지 확인하는 코드
  n=12
  if n in list1:
      print('{}가 리스트에 있다.'.format(n))
  ```

#### 리스트에서 필요 없는 값을 지우는 방법

- del을 이용해서 특정 위치의 값을 지우기
  - `del list1[10]` 리스트의 10번째 값을 지워라
- remove를 이용해서 특정 값을 지우기
  - `list1.remove(40)`을 하면 리스트에 40이라는 값이 있는경우 삭제
  - 여러개의 값이 있는 경우 가장 앞에 있는 하나만 지워짐



## 7. for 반복문

### 7-1 for in list

#### for in 반복문

- 코드를 필요한만큼 반복해서 실행

  ```
  for pattern in patterns:
      print (pattern)
  ```

1. 리스트 patterns의 값을 하나씩 꺼내 pattern으로 전달
2. 리스트의 길이만큼 print (pattern) 실행



### 7-2 for in range

#### range 함수

- 필요한 만큼의 숫자를 만들어내는 유용한 기능

```
for i in range(5):
    print(i)
```

#### enumerate

- 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능

```
names = ['철수', '영희', '영수']
for i, name in enumerate(names):
    print('{}번: {}'.format(i + 1, name))
```



## 8. 모듈

### 8-1 모듈 사용하기

#### 모듈

- 미리 만들어진 코드를 가져와 쓰는 방법

- import 모듈이름

- 사용 방법: 모듈이름.모듈안의 구성요소

  ```
  math.pi
  random.choice()
  ```

#### 모듈의 예

- import math
  - 수학과 관련된 기능
    - math.ceil() : 올림함수
    - math.round() : 반올림함수
    - math.floor() : 내림함수
- import random
  - 무작위와 관련된 기능
    - random.choice() : ()안에 넣은 리스트 중 random으로 출력하는 함수 
- import urllib.request
  - 인터넷의 내용을 가져오는 기능

- **URL을 넣으면 페이지 내용을 불러오는 코드**

```python
def get_web(url):
    """URL을 넣으면 페이지 내용을 불러오는 함수"""
    import urllib.request
    response = urllib.request.urlopen(url)
    data = response.read()
    decoded = data.decode('utf-8')
    return decoded

url = input('웹 페이지 주소를 입력해주세요 : ')
content = get_web(url)
print(content)

```



### 8-2 모듈 만들기

#### 모듈 만들기

1. 사용할 함수, 메소드 코드를 작성한 모듈 파일을 생성
2. 모듈이 쓰일 파일에 import를 사용하여 모듈을 호출
3. 사용 방법은 기존의 모듈과 동일
4. **주의할 점은 사용자가 만든 모듈과 모듈을 쓸 파일이 같은 폴더에 있어야 한다.**

![module_create](https://user-images.githubusercontent.com/38130934/50572908-c50ef900-0e0c-11e9-8a2b-91c5fb17311c.PNG)

출처 : https://programmers.co.kr/learn/courses/2/lessons/185



## 9. 활용하기

### 9-1 검색하기

#### 프로그래밍 검색 요령

1. 검색은 구글
2. 키워드에 파이썬3 또는 python3을 포함하라
3. 코드를 포함한 글을 찾도록 하라
4. 간단한 예제는 REPL을 사용하여 예제를 테스트 해보라
5. 영어를 못해도 영어로 검색하라



### 9-2 문서찾기

#### 공식문서

- 필요한 내용을 둘러보고 싶을때
- 파이썬 내장 모듈과 함수의 정보가 필요할 때
- **site = docs.python.org**

#### 구글 또는 stackoverflow.com

- 문제의 구체적인 해결 방법이 알고 싶을 때
- 구글 검색시 사이트 제한 기능 활용
- **site = stackoverflow.com**



## 10. 딕셔너리와 튜플