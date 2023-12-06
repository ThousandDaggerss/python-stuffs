import datetime


now = datetime.datetime.now()
#  print(now)  # 2022-06-29 17:09:14.245837
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
hour = lambda x: x.time()

print(year(now))  # 2022
print(month(now))  # 6
print(day(now))  # 29
print(hour(now))  # 17:09:14.245837
