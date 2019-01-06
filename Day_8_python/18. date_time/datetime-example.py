import datetime

start_time = datetime.datetime(2019,2,1)
how_long = start_time - datetime.datetime.now()

print(type(how_long))

print(how_long.days)
print(how_long.seconds)

print("2월 1일까지는 {}일 {}시간이 남았습니다.".format(how_long.days, how_long.seconds//3600))
