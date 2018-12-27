## 멋사 스터디 3일차

1. Flexbox
2. CSS Grid

### 1. Flexbox

#### 1-1 Flexbox가 생겨난 이유

> 기본 css로 값을 맞추려고하면 시간도 오래걸리고 화면사이즈가 줄어들면 맞춰놨던 사이즈들이
>
> 깨지는 현상이 발생하기 때문이다.

#### 1-2 Basics of Flexbox

* flex-container와 flex-items는 직접적으로 **종속관계**에 있어야 한다.

> flexbox를 좋아하는 이유
>
> 아무런 계산 필요없이 컴퓨터가 알아서 간격을 나눠준다.
>

##### justify-content 옵션

* flex-start (default) : 처음부터 정렬

  ![flex-start](https://user-images.githubusercontent.com/38130934/50469193-b7add500-09ee-11e9-8211-c844421e6315.PNG)

* flex-end : 끝쪽에서 부터 정렬

  ![flex-end](https://user-images.githubusercontent.com/38130934/50469233-d9a75780-09ee-11e9-9c49-71ad0cd0099e.PNG)

* center :  중앙

  ![center](https://user-images.githubusercontent.com/38130934/50469246-e926a080-09ee-11e9-8fc0-a24c8d73cd97.PNG)

* space-between : 간격을 계산해서 정렬

  ![space-between](https://user-images.githubusercontent.com/38130934/50469258-f774bc80-09ee-11e9-8db3-2de1e92feb63.PNG)

* space-around : 정렬

  ![space-around](https://user-images.githubusercontent.com/38130934/50469272-00fe2480-09ef-11e9-933f-2b6dba1d4023.PNG)

#### 1-3 Main Axis and Cross Axis

##### align-items 옵션 

* stretch (default) 

  ![stretch](https://user-images.githubusercontent.com/38130934/50469459-cba60680-09ef-11e9-9b8d-06e28b398b15.PNG)

* flex-start 

  ![flex-start_2](https://user-images.githubusercontent.com/38130934/50469482-f5f7c400-09ef-11e9-89fc-c7d178932d48.PNG)

* flex-end 

  ![flex-end 2](https://user-images.githubusercontent.com/38130934/50469488-fdb76880-09ef-11e9-820d-0b662a7a36fe.PNG)

* center 

  ![center 2](https://user-images.githubusercontent.com/38130934/50469495-04de7680-09f0-11e9-8852-67e3ae0377b3.PNG)

##### flex-direction 옵션

* raw (default) : 기본값

  ![row](https://user-images.githubusercontent.com/38130934/50469624-99e16f80-09f0-11e9-87e6-baccb0c152b6.PNG)

* raw-reverse

  ![raw-reverse](https://user-images.githubusercontent.com/38130934/50469629-a1a11400-09f0-11e9-8760-b52d558ec0c4.PNG)

* column

  ![column](https://user-images.githubusercontent.com/38130934/50469639-abc31280-09f0-11e9-95d7-32502add1880.PNG)

* column-reverse 

  ![column-reverse](https://user-images.githubusercontent.com/38130934/50469643-afef3000-09f0-11e9-9bfd-e5cbf575cac5.PNG)

**flexbox direction  = row , main(수평) / cross(수직)**

**flexbox direction = column, main(수직) / cross(수평)**

#### 1.4 Flex Wrap and Direction

##### flex-wrap 옵션 

* no-wrap (default)

  ![no-wrap](https://user-images.githubusercontent.com/38130934/50469751-2ab84b00-09f1-11e9-8128-6c29df68bc77.PNG)

* wrap : 자기가 정한 크기가 화면보다 넘어가면 그 다음에 생성 

  ![wrap](https://user-images.githubusercontent.com/38130934/50469754-30ae2c00-09f1-11e9-9a0a-0f369c7823d1.PNG)

* wrap-reverse

  ![wrap-reverse](https://user-images.githubusercontent.com/38130934/50469762-399efd80-09f1-11e9-8419-124dd2cfb3aa.PNG)

#### 1.5 Align Self and Flexbox Conclusions

flex-container에게 주는 것이 아닌 flex-item에게 영향을 미침

##### align-self