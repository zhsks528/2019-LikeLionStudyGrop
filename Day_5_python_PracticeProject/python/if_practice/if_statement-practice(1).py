from datetime import datetime
hour = datetime.now().hour

if hour < 12:
    print('오전입니다.')
