import datetime
import time
import calendar


#  with datetime module
readdatetime = datetime.datetime.fromtimestamp(1629071354).isoformat()

print(readdatetime)  # 2021-08-15T20:49:14

#  with time module
readtime = time.ctime(1629071354)  # Sun Aug 15 20:49:14 2021

print(readtime)

ts = time.gmtime()

print(time.strftime("%Y-%m-%d %H:%M:%S", ts))  # 2021-08-28 05:57:39

print(time.strftime("%x %X", ts))  # 08/28/21 05:57:39

# Iso Format
print(time.strftime("%c", ts))  # Sat Aug 28 05:57:39 2021

# Timestamp with calendar module
tsc = calendar.timegm(time.gmtime())
print(tsc)  # 1630130259
