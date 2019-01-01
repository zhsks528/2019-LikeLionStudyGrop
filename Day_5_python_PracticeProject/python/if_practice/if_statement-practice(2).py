#아래 두 줄의 코드는 변수 hour에 현재 시간을 저장합니다.
#이 코드가 어떻게 동작하는지는 이후 강의에서 다룹니다.
from datetime import datetime 
hour = datetime.now().hour

#현재 시간이 6의 배수일 때만 print문이 실행되도록 아래줄에 if문을 추가하세요
if hour % 6 == 0:
    print('종이 울립니다.')#if문을 추가한 이후 이 줄은 들여쓰기 되어야 합니다.
