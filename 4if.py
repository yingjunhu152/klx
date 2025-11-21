#if第1种用法
money1=500
if money1>700:
    print(123)
    print(456)


#if第2种用法
money2=500
if money2>700:
    print(123)
    print(456)
else:print('back')

print(789)

#if第3种用法嵌套
money3=int(input("你有多少钱？"))
if money3>100:
    if money3>150:
        print("吃海底捞+电影")
    else:print("吃个海底捞就走")
else:print("just back home")


#if第4种用法嵌套
money4=int(input("你还有多少钱？"))
if money4>600:
    print(1)
elif money4>500:
    print(2)
elif money4>=400:
    print(3)
elif money4>100:
    print(4)