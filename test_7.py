
X1={'a':1,'b':2}
X2=dict(a=1,b=2)

print(X1)
print(X1.keys())
print(X2)
print(X2.values())
print(X1.pop("a"))
print(X1)
print(X2.popitem())
print(X2)

a={}
b=a.fromkeys((1,2,3),'a')
print(b)

print({i:i*2 for i in range(1,6)})