'''
import random
# 构建一个列表，将大写小写字母和10个数字全部添加进来
list = []
# 生成26个大写字母
for x in range(65, 91):
    a = str(chr(x))  # 生成对应的ASCII码对应的字符串（先从ASCII码转为字符）
    list.append(a)
# 生成26个小写字母
for x in range(97, 123):
    a = str(chr(x))  # 生成对应的ASCII码对应的字符串（先从ASCII码转为字符）
    list.append(a)
for x in range(10):
    list.append(str(x))
def get_code():
    s = ''
    for x in range(2):
        for x in range(16):
            a = random.choice(list)  # 直接从已构建的列表中筛选随机元素返回
            s = s + a
            if len(s) == 16:
                s = s + '\n'
    return s
if __name__ == '__main__':
    print(get_code())
'''
'''
result=0
for i in range(1,101,2):
    result=result+i
    print(i)
    print(result)
'''
'''
a=1
while a<=100:
    print(a)
    a=a+1
else:print("a大于100")
'''
'''
for i in range(1,11):
    # if i == 5:
        # break
        # continue
    print(i)
'''
'''
import random
computer_no = random.randint(1,100)
# print(computer_no)
while 1==1:
    person_no = int(input("请输入一个数字："))
    if person_no < computer_no:
        print("太小了，大一点！")
    elif person_no > computer_no:
        print("太大了，小一点！")
    else:
        print("太棒了，猜对了！")
        break
'''
