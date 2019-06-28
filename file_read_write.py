#文件读写的3中模式
# 1、w 写模式，它是不能读的，如果用w模式打开一个已经存在的文件，会清空以前的文件内容，重新写
#    w+ 是读写内容，只要沾上w，肯定会清空原来的文件
# 2、r 读模式，只能读，不能写，而且文件必须存在
#    r+ 是读写模式，只要沾上r，文件必须存在
# 3、a 追加模式，也能写,在文件的末尾添加内容
# 4、rb+、wb+、ab+,这种是二进制模式打开或者读取，一些音乐文件

#readlines是读取该文件的所有内容，readline是读取首行内容
# \n表示换行
with open("E:/1.txt",'r+') as file:
    file.write('32\n')
    file.write("end")
    line=file.readlines()
    print(line)

names =["LuFei","SuoLong",["Luo","JiDe"],"XiangJiShi","QiaoBa"]

names .append("WuSuoPu")#追加
print(names) #['LuFei', 'SuoLong', ['Luo', 'JiDe'], 'XiangJiShi', 'QiaoBa', 'WuSuoPu']

file.seek(0) # 移动文件指针
file.truncate() # 清空文件内容

