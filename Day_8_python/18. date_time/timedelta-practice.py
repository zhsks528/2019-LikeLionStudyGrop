import datetime

hundred_after = datetime.datetime.now().replace(hour = 9, minute = 0, second = 0) + datetime.timedelta(days=100)

print("{}/{}/{}  {}:{}:{}".format(hundred_after.year,hundred_after.month, hundred_after.day, hundred_after.hour, hundred_after.minute, hundred_after.second))
