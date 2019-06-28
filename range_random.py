import random
print(random.randrange(3,9,2))  #步长为2，也就是返回3-9区间的随机奇数，包括3，不包括9
#1、：返回0-1之间的随机浮点数
random.random()
#random.uniform(a,b),返回限定范围的随机浮点数，a和b可以是浮点数，也可以是整数
print(random.uniform(1.2,3.6))
#random.randint(a,b):返回限定范围内的整数，包括a和b
print(random.randint(1,8))
#random.randrange(start, stop=None, step=1),
# 按步长step返回范围内随机整数，随机数包括左区间的起始值，不包括右区间的结束值
print(random.randrange(3,9,2))  #步长为2，也就是返回3-9区间的随机奇数，包括3，不包括9
#random.choice(seq)：从序列中随机选择一个元素
print(random.choice(['123',4,6,9,8]))
#random.sample(seq,k):从序列中选取指定个数的元素
print(random.sample([1,6,3,9,8],2)) #[3, 9]
#random.shuffle(seq)：把一个序列元素顺序打乱，俗称“洗牌”
import random
a = [1,6,3,9,8]
random.shuffle(a)
print(a) #结果[6, 8, 3, 1, 9]

#生成一个包括数字和字母的5位验证码。
def v_code():
    code =''
    for i in range(5):
        s = random.choice([random.randrange(10),chr(random.randrange(65,91))])
        code += str(s)
    return code
