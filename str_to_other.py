s1 = "['name','leo']"
s_list = eval(s1)    #字符串转换为列表
print(s_list[1])

s2 = "{'name':'leo','age':32}"
s_dict = eval(s2)    #字符串转换为字典
print(s_dict['name'])

s3 = "{1,2,3,4}"
s_set = eval(s3)    #字符串转换为集合
print(s_set.remove(4))
s4 = "(1,2,3,4)"
s_tuple = eval(s4)    #字符串转换为元组
print(s_tuple[1])