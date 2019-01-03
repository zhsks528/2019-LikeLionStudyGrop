## Day_1

**Prettier - Code formatter : 코드를 정리하는 확장 패키지**

**django Template:**





settings (JSON) : 개인적으로 수정하기 ^^...



**프로젝트를 생성하는 명령어**

django-admin startproject <프로젝트명>



**django-package 는 오픈소스 개념이라고 생각하면된다.**



**앱만들기**

1. python manage.py startapp <앱 명>
2. settings.py에 앱 명을 추가한다.
3. urls.py에 import 해줘야한다.



**겹치면 as 를 써서 별명을 지어준다!**



**html파일을 렌더링 하는 방법**

1. templates폴더를 생성
2. 그 밑에 폴더를 생성
3. 파일명.html 파일 생성후 작성
4. **views.py** 에 소스코드작성

예.

```
from django.structor import render

def 함수명(request):

	return render(request, '폴더명/파일명.html')


```



**model 생성하기**

```
class 클래스명 (models.Model):
	title = modles.CharField(max_length=20) #최대 길이 제한 20
	content = models.TextField()
	users = models.CharField(max_length=30)
```



**마이그레이션 만들기**

**python manage.py makemigrations <앱 명>**

--반영이 되기전임

**python manage.py migrate <앱 명>**을 해야 반영이 됨.



**관리자 페이지에 등록하기**

admin.py에  admin.site.register(앱 명)



**createsuperuser 생성하기**

python manage.py createsuperuser



**만약 생성이 안되면?**

**winpty** python manage.py createsuperuser



def __ str __(self):

​	return self.title



> class- > 설계도 
>
> Instance ->  실제, 물체, 건축물



**실행**

python manage.py runserver 

