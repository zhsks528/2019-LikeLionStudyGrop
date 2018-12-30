## 멋사 스터디 4일차





#### 1. Parcel 설치 및 적용방법

> **https://paceljs.org 참고**
>
> 장점 :  이전과는 다르게 서버를 이용하기 때문에 소스코드를 바꾸면 바로 적용되는 것을 볼 수 있다.



1. ```
   $ npm init -y
   ```

2. ```
   $ npm install -g parcel-bundler
   ```

3. **package.json에서 script 부분에 start 부분 추가**

![parcel](https://user-images.githubusercontent.com/38130934/50546353-dd92de00-0c69-11e9-9f4f-c4c5964ba08e.png)



#### 2. Post CSS 와 Parcel

> PostCSS는 CSS를 조금 더 현대적으로 바꿔주는 방법
>
> 코드를 자동변환 해준다.
>
> **https://preset-env.cssdb.org/ 참고**



#### 설치방법

1. ```
   $ npm install postcss-preset-env
   ```

2. **package.json에 추가해준다.**

![postcss](https://user-images.githubusercontent.com/38130934/50546499-de2c7400-0c6b-11e9-9d23-2444b6a3f762.PNG)



#### 3. Functional pseudo-classes

> CSS를 함수처럼 작동하는 방법 (여러가지가 있음)



```
li:matchs(:nth-child(even), . target) {

	background-color : blue;

}
```

![pseudo-classes_1](https://user-images.githubusercontent.com/38130934/50546627-0ae18b00-0c6e-11e9-8c2c-15ea9176f0dd.PNG)



```
li:not(. target) {

	background-color : blue;

}
```

![pseudo-classes_2](https://user-images.githubusercontent.com/38130934/50546630-1765e380-0c6e-11e9-9bc9-fb7461a44641.PNG)



#### 4. CSS Variables

