lo=int(input('上限：'))1
hi=int(input('下限：'))
for i in range(lo,hi+1):
    if i > 1:
        for j in range(2,i):
            if (i % j) == 0:
                break
        else:
            print(i)
print("Hello World!")

##版权声明：本文为CSDN博主「超级大黄狗Shawn」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
##原文链接：https://blog.csdn.net/weixin_41084236/article/details/81564963