# 멋사 스터디 2일차 공부

1.  branch
2.  Github
3.  My server

## 1-1 branch 만들기

* **브랜치의 목록을 볼 때**

```
$ git branch
```

* **브랜치를 생성할 때**

```
$ git branch "새로운 브랜치 이름"
```

* **브랜치를 전환(체크아웃)할 때**

```
$ git checkout "전환하려는 브랜치 이름"
```

* **브랜치를 삭제할 때**

```
$ git branch -d
```

* **병합하지 않은 브랜치를 강제 삭제할 때**

```
$ git branch -D
```

* **브랜치를 생성하고 전환까지 할 때**

```
$ git checkout -b "생성하고 전환할 브랜치 이름"
```



## 1-2 branch 정보확인

* **브랜치 간에 비교할 때**

```
$ git log "비교할 브랜치 명 1"..."비교할 브랜치 명 2"
```

* **브랜치 간의 코드를 비교 할 때**

```
$ git diff "비교할 브랜치 명 1"..."비교할 브랜치 명 2"
```

* **로그에 모든 브랜치를 표시하고, 그래프로 표현하고, 브랜치명을 표시할 때**

```
$ git log --branches --graph --decorate
```

* **로그에 모든 브랜치를 표시하고, 그래프로 표현하고, 브랜치 명을 표시하고, 한줄로 표시할 때**

```
$ git log --branches --graph --decorate --oneline!
```



## 1-3 branch 병합

* **A  브랜치로 B 브랜치를 병합할 때(A←B) 순서**

1.  master에다가 exp를 merge하려면 

2.  git checkout master 명령어를 입력하여 branch를 master로 바꿔준다

   ```
$ git checkout master
   ```

3.  git merge exp 명령어 실행

   ```
$ git merger exp
   ```



## 1-4 branch 병합 시 충돌해결

* **같은 부분을 수정하면 충돌이 일어남**

충돌이 생기면 아래와 같은 메시지가 생성![collision](F:\바탕화면\collision.PNG)



**git status**를 하면 충돌이 일어난 파일을 찾을 수 있다.![collision2](F:\바탕화면\collision2.PNG)



충돌이 발생한 파일을 수정한다.



 '<<<<<<< HEAD' 부터 '=======' 사이의 구간이 현재 체크 아웃된 파일의 내용이고 '=======' 부터 '>>>>>>> exp' 사시의 구간이 병합하려는 대상인 exp 브랜치의 코드 내용이다. 이 정보를 참고로해서 두개의 코드를 병합한 후에 특수기호들을 제거하면된다.

작업이 끝나면 파일을 저장한다



## 1-5 statsh

* 사전적 의미 : 감추다

다른 브랜치로 checkout을 해야 하는데 현재 브랜치에서 작업이 끝나지 않은 경우는 커밋을 하기가 애매하다! 

**(다른 브랜치로 이동하면 현재 브랜치에서 작업중이던 파일이 영향을 미침)**

이런 경우 **stash**를 이용하면 작업중이던 파일을 임시로 저장해두고 현재 브랜치의 상태를 마지막 커밋의 상태로 초기화 할 수 있다.

```
$ git stash
```

* **임시로 저장해둔 걸 불러오는 명령어**

```
$ git stash apply
```

* **stash의 목록을 보는 명령어**

```
$ git stash list
```

> *stash는 스택처럼 쌓인다. git apply는 최신 stash로 돌려준다*

- **stash list의 스택을 지우는 명령어**

```
$ git stash drop
```

- **apply 후 지우고 싶다면**

```
$ git stash pop
```



---



## 2-1 원격 저장소를 지역 저장소로 복제 (Github)

* **어떤 소스코드를 로컬저장소로 가져오는 명령어**

```
$ git clone <저장하고 싶은 github의 주소>
```

* **로그를 거꾸로 출력하기**

```
$ git log --reverse 
```

* **첫번째 커밋으로 체크아웃하기**

```
$ git checkout "commit -id 입력"
```



## 2-2 원격저장소 만들기(Github)

Github 회원가입을 해야함

Public : 오픈소스 / 무료

Private : 개인소스 / 유료 

Initialize this repository with a README : 프로젝트에 대한 기본 설명 파일을 만드는 것

---

* **원격 저장소를 등록하는 명령어**

```
$ git remote add <이름> <github 주소>
```

* **원격 저장소 리스트를 보는 명령어**

```
$ git remote -v
```

* **원격 저장소로 등록한 이름과 주소 삭제**

```
$ git remote remove <원격저장소 이름>
```

* **앞으로 현재 브랜치를 원격저장소 <이름>의 master에 동기화 시키는 명령어**

```
$ git push -u <이름> master
```



## 2-3 원격 저장소와 지역 저장소의 동기화 방법 (Github)

1. ```
   $ git clone <저장하고 싶은 github의 주소>
   ```

2. ```
   $ git remote add <이름> <github주소>
   ```

3. ```
   $ git pull <이름> master
   ```

4. ```
   $ git add <작업한 내용들>
   ```

5. ```
   $ git commit -m "commit 날리기"
   ```

6. ```
   $ git push
   ```



## 2-4 로그인 없이 원격 저장소 이용하기 (Github)

ssh = Secure Shell

나중에 추가하겠습니다...



## 3-1 자기서버에 원격 저장소 만들기 (My Server)

나중에 추가하겠습니다...



## 3-2 push & pull (My Server)

집에서 작업을 한다 (파일작업 / add / commit / push)

회사에서 작업을 한다. 이 때 집에서 했던 작업을 가지고 오고싶다. (git pull)

push & pull 를 사용할 때 주의할 점 : push를 하기전에 pull 을 해야한다.

[rejected] 발생 

**[rejected] 해결 방법**

**git pull 을 하면 병합으로 넘어간 후 gi t push를 하면된다.**



## 3-3 자동 로그인 (My Server)

 나중에 추가하겠습니다...