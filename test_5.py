
X1=1,2,3
X2=(1,2,3)
X3=[1,2,3]
X4={1,2,3}

print(X1)
print(type(X1))
print(X2)
print(type(X2))
print(X3)
print(type(X3))
print(X4)
print(type(X4))

X3[0]="ZK"
print(X3)
X5=(34,3334,432,X3)
print(id(X5[3]))
print(X5)
X5[3][0]='hello'
print(id(X5[3]))
print(X5)


X6=(1,2,3,4,'c','c','b','c','c','b')
print(X6.count('b'))
print(X6.index('b'))
print(id(X6[3]))
print(id(X6[X6.index(4)]))