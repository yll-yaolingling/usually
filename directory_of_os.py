import os

#获取文件名或者文件后缀
file="we.txt"
filename=os.path.splitext(file)
print(filename[0])#获取文件名
print(filename[1])#获取文名件后缀

#列出路径下的所有文件夹和文件,os.listdir() 方法用于返回指定的目录下包含的文件或子目录的名字的列表。
# 这个列表以字母顺序。其得到的是仅当前路径下的文件名，不包括子目录中的文件，如果需要得到所有文件需要递归。 它也不包括 '.' 和 '..' 即使它在目录中。
os.listdir("E:/")

#os.walk() 方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下。是一个简单易用的文件、目录遍历器，可以帮助我们高效的处理文件、目录方面的事情。
#os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])

os.path.exists()#判断文件或目录是否存在

os.path.isfile()#判断是否是文件

os.path.isdir()#判断是否是目录

os.path.dirname()#获取当前文件所在的目录，即父目录

os.makedirs()#创建多级目录

os.mkdir()#创建单级目录

os.path.getsize()#获取文件大小
