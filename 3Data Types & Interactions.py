a=10
b=20
print(a+b)

c=1.25
print(4*c) 

s='旭哥'
print(s)

d='''woc
nb
wocnb
'''
print(d)
k='太帅了'
print(s+k)
print(2*s)

#布尔值
print(100>30)
print(100<30)
l=100<30
print(l)

a1=input("请输入第一个数字")
a2=input("请输入第二个数字")
#print(a1+a2)
#因为是a1和a2是字符串，要把字符串转化为其他类型，，想把谁转化成谁，就把谁套起来
a1=int(a1) 
a2=int(a2)
print(type(a1))
print(a1+a2)