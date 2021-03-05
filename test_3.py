"""
def method(**a):
    print(a.keys())
    # return a
method(a=1,b=2,c=3,d=4)
"""
"""
def method(*a):
    print(a[0])
    print(a[1])
    print(a[2])
method(1,2,3)
"""
"""
def method(*,a):
    print(a)   
method(a=1)
"""
"""
def method(a,b=[]):
    b.append(a)
    return b
print(method(1))
print(method(3))
print(method(5))
"""
# print(list(range(3,6)))
"""
list_a = (1,4)
print(list(range(*list_a)))

def method(a,b,c):
    print(a),print(b),print(c)
dic1={"a":1,"b":2,"c":3}
method(**dic1)
"""
"""
a = lambda x,y,z:x*2+y*3+z*4
print(a(2,3,1))
"""

list_a=[35,14,59,742]
list_a.append(7)
list_a.insert(4,91)
y=list_a.pop(0)
list_a.remove(59)
#list_a.sort(reverse=True)
#list_a.reverse()
print(y)
print(list_a)
