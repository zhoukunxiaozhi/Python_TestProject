# try:
#     a = int(input("请输入一个被除数："))
#     b = int(input("请输入一个除数："))
#     print(a / b)
# except ZeroDivisionError:
#     print("除数不能为0！他妈的错了")
# except ValueError:
#     print("需要输入数值型整数")
# except:
#     print("这是一个异常！")
# else:
#     print("执行完毕")
# finally:
#     print("无论是否发生异常，都会有此提示")


# x=10
# if x>5:
#    raise Exception("这是抛出的异常信息")

class MyException(Exception):
    def __int__(self,a,b):
        self.a = a
        self.b = b

raise MyException("x","y")