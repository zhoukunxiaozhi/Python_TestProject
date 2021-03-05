'''
class Person1:
    name="Hello,Jerry!"

    def get_name(self):
        return self.name

print(Person1.name)

p=Person1()
print(p.name)
print(Person1.name)

Person1.name="lili"
print(Person1.name)
print(p.name)
p.name="xiaoming"
print(Person1.name)
print(p.name)
Person1.name="Tom"
print(Person1.name)
print(p.name)

q=Person1()
print(Person1.name)
print(q.name)
'''

class Person2:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def only(self,value):
        self.value = value
    def desc(self):
        print("我叫%s，今年%d岁，是名%s" % (self.name,self.age,self.sex))

xiaoming=Person2("小明",13,"男性")
xiaohong=Person2("小红",10,"女性")
tom=Person2("Tom",12,"男性")

print(xiaoming.name)
print(xiaohong.age)
print(tom.sex)

xiaoming.only("Fit")
print(xiaoming.value)

xiaoming.desc()
xiaohong.desc()
tom.desc()