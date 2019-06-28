import os
testdir="D:\\"
lists=os.listdir(testdir)
lists.sort(key=lambda fn:os.path.getmtime(testdir+'\\'+fn))
dir=os.path.join(testdir,lists[-1])
print(dir)
