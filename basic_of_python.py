
#和用户的交互input()
name=input("input name")
print(name)

#打印不换行
print("ssdf",end="")

#带格式输出
name="we"
age=12
print("name=%s age=%d" %(name,age))
print("my name is %s ,and age is %d" %(name,age))

# 第一种结合多行打印可以实现用户交互，利用字符拼接’’’ + 变量 +’’’
name = input("name:")
age = input("age:")
job = input("job:")
salary = input("salary:")

info = '''
----------info of ''' + name + ''' ----------
Name:'''+ name + '''
Age:'''+ age + '''
Job:''' + job + '''
Salary:''' + salary
print(info)

#格式化输出，.format（），建议使用
info = '''
---------- info of {_name} ----------
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
'''.format(_name=name ,
            _age=age,
            _job=job ,
           _salary=salary)

print('{},{}'.format('kzc',18))
#输出'kzc,18'

#if
#if   elif
#if   else

#切片取文件名
t="file1.txt"
print(t[:-4])

#
sdict={
    "a":{"a1","a2","a3"},
    "b":{"b1","b2","b3"},
    "c":{"c1","c2","c3"}
}
s=input("select")
ss=sdict.get(s)
s2=sdict[s]
sdict['d']=["d1","d2"]
print (sdict)

#字典的嵌套
x=[{'close': '0.1021','datetime': '2018-10-12 15:21:00',
 'high': '0.1021',
 'low': '0.1021',
 'open': '0.1021',
 'time': '1539328860000',
 'volume': '1643.3757'},
{'close': '0.1021',
 'datetime': '2018-10-12 15:20:00',
 'high': '0.1021',
 'low': '0.1021',
 'open': '0.1021',
 'time': '1539328800000',
 'volume': '4232.6447'},
{'close': '0.1019',
 'datetime': '2018-10-12 15:18:00',
 'high': '0.1019',
 'low': '0.1019',
 'open': '0.1019',
 'time': '1539328680000',
 'volume': '2909.9173'},]
n=len(x)
for i in range(0,n):
    print(i)
    print(x[i].keys())