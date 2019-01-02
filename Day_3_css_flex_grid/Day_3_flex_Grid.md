## 멋사 스터디 3일차

1. Flexbox
2. CSS Grid

## 1. Flexbox

### 1-1 Flexbox가 생겨난 이유

> 기본 css로 값을 맞추려고하면 시간도 오래걸리고 화면사이즈가 줄어들면 맞춰놨던 사이즈들이
>
> 깨지는 현상이 발생하기 때문이다.

### 1-2 Basics of Flexbox

* flex-container와 flex-items는 직접적으로 **종속관계**에 있어야 한다.

> **flexbox를 좋아하는 이유**
>
> 아무런 계산 필요없이 컴퓨터가 알아서 간격을 나눠준다.
>

#### justify-content 옵션

* flex-start (default) : 처음부터 정렬

  ![flex-start](https://user-images.githubusercontent.com/38130934/50469193-b7add500-09ee-11e9-8211-c844421e6315.PNG)

* flex-end : 끝 쪽에서 부터 정렬

  ![flex-end](https://user-images.githubusercontent.com/38130934/50469233-d9a75780-09ee-11e9-9c49-71ad0cd0099e.PNG)

* center :  중앙에서부터 정렬

  ![center](https://user-images.githubusercontent.com/38130934/50469246-e926a080-09ee-11e9-8fc0-a24c8d73cd97.PNG)

* space-between : 간격을 계산해서 정렬

  ![space-between](https://user-images.githubusercontent.com/38130934/50469258-f774bc80-09ee-11e9-8db3-2de1e92feb63.PNG)

* space-around : 일정한 여백을 두고 정렬

  ![space-around](https://user-images.githubusercontent.com/38130934/50469272-00fe2480-09ef-11e9-933f-2b6dba1d4023.PNG)

### 1-3 Main Axis and Cross Axis

#### align-items 옵션 

* stretch (default) 

  ![stretch](https://user-images.githubusercontent.com/38130934/50469459-cba60680-09ef-11e9-9b8d-06e28b398b15.PNG)

* flex-start : 맨 윗줄부터 시작

  ![flex-start_2](https://user-images.githubusercontent.com/38130934/50469482-f5f7c400-09ef-11e9-89fc-c7d178932d48.PNG)

* flex-end : 맨 아래부터 시작

  ![flex-end 2](https://user-images.githubusercontent.com/38130934/50469488-fdb76880-09ef-11e9-820d-0b662a7a36fe.PNG)

* center : 중간에서부터 시작

  ![center 2](https://user-images.githubusercontent.com/38130934/50469495-04de7680-09f0-11e9-8852-67e3ae0377b3.PNG)

#### flex-direction 옵션

* raw (default) : 가로로 방향을 지정

  ![row](https://user-images.githubusercontent.com/38130934/50469624-99e16f80-09f0-11e9-87e6-baccb0c152b6.PNG)

* raw-reverse : raw의 역순으로 설정

  ![raw-reverse](https://user-images.githubusercontent.com/38130934/50469629-a1a11400-09f0-11e9-8760-b52d558ec0c4.PNG)

* column : 세로로 방향을 설정

  ![column](https://user-images.githubusercontent.com/38130934/50469639-abc31280-09f0-11e9-95d7-32502add1880.PNG)

* column-reverse : column 방향의 역순으로 설정

  ![column-reverse](https://user-images.githubusercontent.com/38130934/50469643-afef3000-09f0-11e9-9bfd-e5cbf575cac5.PNG)

> **flexbox direction  = row , main(수평) / cross(수직)**
>
> **flexbox direction = column, main(수직) / cross(수평)**

### 1.4 Flex Wrap and Direction

#### flex-wrap 옵션 

* no-wrap (default)

  ![no-wrap](https://user-images.githubusercontent.com/38130934/50469751-2ab84b00-09f1-11e9-8128-6c29df68bc77.PNG)

* wrap : 자기가 정한 크기가 화면보다 넘어가면 그 다음 줄에 생성

  ![wrap](https://user-images.githubusercontent.com/38130934/50469754-30ae2c00-09f1-11e9-9a0a-0f369c7823d1.PNG)

* wrap-reverse : wrap에서 순서를 반대로 설정

  ![wrap-reverse](https://user-images.githubusercontent.com/38130934/50469762-399efd80-09f1-11e9-8419-124dd2cfb3aa.PNG)

### 1.5 Align Self and Flexbox Conclusions

#### **flex-container에게 주는 것이 아닌 flex-item에게 영향을 미침**

#### align-self 옵션 (Blue를 설정했다고 가정)

* flex-start : 맨 위에서부터 시작하도록 설정

  ![flex-start_3](https://user-images.githubusercontent.com/38130934/50470503-1033a100-09f4-11e9-83c1-b2153474a26d.PNG)

* flex-end : 맨 아래에서부터 시작하도록 설정

  ![flex-end_3](https://user-images.githubusercontent.com/38130934/50470528-322d2380-09f4-11e9-82c0-d46d68f2e0c6.PNG)

* stretch : 전부 채우도록 설정

  ![flex-stretch](https://user-images.githubusercontent.com/38130934/50470540-39543180-09f4-11e9-9078-67240b94c0ee.PNG)

* center : 중앙에서부터 시작하도록 설정

  ![center-3](https://user-images.githubusercontent.com/38130934/50470543-3e18e580-09f4-11e9-8755-e496bd6bd693.PNG)



flex를 사용하여 개구리를 옮기는 사이트 : https://flexboxfroggy.com/#ko

**출처 : w3shools.com**



## 2. Grid

### 2-1 Why we need Grid

> **flex가 충분하지 않은 이유**
>
> 웹사이트에서 필요로 하는 레이아웃을 짜기가 힘듬



### 2-2 Basics CSS Grid 

> Grid는 row와 column 개념이 반대

**grid-template-rows** : 세로를 설정

**grid-template-columns** : 가로를 설정

**grid-gap** : 객체간의 여백을 설정



### 2-3 Auto Rows and Columns

설정해 놓은 rows와 columns보다 더 많은 element들이 만들어져서 자리에 맞지 않는다면 나머지의 element의 자리는 auto rows/columns로 설정 해줄 수 있다.

```
grid-auto-rows : 60px
```

나머지 element의 rows를 60px로 지정하겠다는 이야기이다. column은 기존에 설정 했던 값으로 정렬된다.

```
gird-auto-columns : 60px;
```

나머지 element의 columns를 60px로 지정하겠다는 이야기이다. rows는 기존에 설정 했던 값으로 정렬된다.

```
gird-auto-flow : row;
```



### 2-4 Grid Template Areas

```
gird-template-areas: "header header header"
					 "content content sidebar"
					 "content content sidebar"
					 "footer footer footer";
```



### 2-5 fr and repeat()

* fr = fraction  비율을 정함 

* repeat()

> ex) grid-tempate-column : repeat(4, 1fr) 4개를 1:1:1:1 가로 비율로 레이아웃을 설정해라
>
> 첫번째 인자는 몇개를 반복할 것인가를 적으면 된다
>
> 두번째 인자는 비율을 적으면 된다.



### 2-6 minmax, max-content, min-content

- minmax : 어느 지점에선 그 상태를 유지하라는 말을 뜻함

```
grid-template-columns:minmax(400px, 2fr) repeat(3, 1fr);
```

- max-content : 최대한 늘어날 수 있을만큼 늘어나라는 말을 뜻함

```
grid-template-columns:max-content repeat(3, 1fr);
```

- min-content : 최대한 줄일 수 있을만큼 줄이라는 말을 뜻함

```
grid-template-columns:min-content repeat(3, 1fr);
```



### 2-7 auto-fill, auto-fit

```
grid-template-columns:repeat(auto-fill,50fr);
```

fraction하나가 전체의 공간을 다 차지하게 되는 것이다. 위의 코드는 가질 수 있는 가장 많은 column을 가지되 50px로 하겠다는 의미이다.

```
grid-template-columns:repeat(auto-fill,340fr);
```

340px크기로 이루어진 div를 다섯번 반복 할 수 없기 때문에 나누어서 밑으로 들어간다.

단점은 크기에 대한 유연성이 없다는 것이다.

```
grid-template-columns:repeat(auto-fit, minmax(350px,1fr));
```

이런 문제점을 보완하기 위해 minmax를 쓴다. 최소값은350px로 지정하고 최대값을 1fr로 지정된다.

```
grid-template-columns:repeat(auto-fill, minmax(50px,1fr));
```

auto-fill은 기존에 있는 layout을 채워나가는 방식으로 가능한 많은 cell로 container을 꽉 채우는데 gost grid가 생길 수 있다.

```
grid-template-columns:repeat(auto-fit, minmax(50px,1fr));
```

ghost grid를 만들지 않고 content를 받아와서 빈자리를 모두채울 때 까지 펼쳐준다.



### 2-8 Jusify Content, Align Content and Place Content

```
justify-item: center;
```

container은 그대로 이고 그 안의 item만을 움직이다.

만약 box안의 item이 숫자 2였다면 박스의 넓이를 기준으로 정중앙으로 2가 정렬되는 것이다.

```
align-item: center;
```

만약 box안의 item이 숫자 2였다면 박스의 높이를 기준으로 정중앙으로 2가 정렬되는 것이다.

```
place-items:
```

첫번째 argument에는 vertical한 값을, 두번째는 horizontal한 값을 넣을 수 있다.

이것이 바로 grid 내부에서 혹은 box내부에서의 element를 움직이는 방법이다.



### 2-8 Justify Items, Align Items and Place Items
