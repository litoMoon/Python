#元组--不可以发生改变
#1.创建元组
a=(1,2,3,4,5,6,7)

#逆序打印
# for i in range(-len(a),0,1):
#     print(a[i])
for i in range(-1,-len(a)-1,-1):
    print(a[i])   #打印出来的结果是 7 6 5 4 3 2 1

#切片
# print(a[-1::-2])  #这个表示从-1开始，后续按照步长为-2，也就是倒着走每两步打印一次
# print(a[::-2])

# b=tuple()
# print(type(a))
# print(type(b))

#元组中的元素一旦确定了就不可以在进行修改了
#所以对元组之后读的操作，没有写的操作
#读取元组中下标为 1 的数据
# print(f"打印原始的元组数据: {a}")
# print(a[1])

#遍历元组--方式一
# for elem in a:
#     print(elem)

#遍历元组--方式二
# for i in range(0,len(a)):
#     print(a[i])

#获取元组中的切片
# print(a[1:4])
# #设置步长
# print(a[1::2])


