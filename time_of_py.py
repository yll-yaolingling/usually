import time
import datetime
t1=time.localtime()
print(t1)
s=time.strftime("%y-%m-%d %H:%M:%S",t1)
print(s)
t2="2017-05-20 08:08:10"
s1=time.strptime(t2,"%Y-%m-%d %H:%M:%S")
print(s1)

#datetime.datetime.now()：打印格式化时间，这种格式大多用于日志打印中
print(datetime.datetime.now())
