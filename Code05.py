# ctrl＋alt＋L 调整格式
# 列表
# 1.创建列表
a = [1, 2, 3, 4, 5, 6]
# print(a)
# print(type(a))
# b=list()
# print(type(b))
#


# # 2.新增元素
# # append()新增到末尾的元素
# b.append(1)
# b.append(2)
# print(b)
# insert 指定位置添加元素
a.insert(4, 401)
a.insert(3, 301)
a.insert(7, 'hello')

#通过访问下标的方式访问元素
print(a)
print(a[2])

# 查找
# 1.使用in判断某个元素在列表中是否存在
# print(2 in a)
# print(10 in a)
# 2.使用 index 判定当前元素在列表的位置
# print(a.index(2))
# print(a.index(5))
#
# #当查找的元素不再当前列表时，会抛出异常 valueError
# print(a.index(500))

# 删除
# 1.使用 pop 删除元素，若没有传入参数，默认删除最后一个
# print(a)
# a.pop()
# print(f"使用pop方法删除最后一个删除之后:{a}")
# 若传入参数，就是删除指定下标位置所在的元素
# 删除下标为3的元素信息
# print(f"未删除元素之前的列表:{a}")
# print(f"下标为3的元素是:{a[3]}")
# a.pop(3)
# print(f"删除下标为3的元素之后，列表元素为:{a}")
# 2.使用 remove 删除元素
# remove 删除的原则是，传入被删除素，不是下标，是元素的值
# print(a)
# a.remove(401)
# print(a)

# 拼接
# 1.使用 ＋ 拼接两个列表，此时会生成一个新的列表，原本的列表数据不会发生变化
# b = ['world', 8, 9, 10]
# c = a + b
# print(c)
# print(a + b)
# print(a)
# print(b)

# 2.使用 extend 可以拼接两个列表，是将后一个列表的元素拼接到前一个列表中
# 会改变前一个列表的值，且使用 extend 方法没有返回值，会直接修改原列表的值
# print(f"a列表原数据值: {a}")
# print(f"b列表原数据值: {b}")
# a拼接b
# c = a.extend(b)
# print(c)  c输出的值为 None
# print(a.extend(b))
# print(a)
# print(b)

#3.使用 += 进行拼接
# a+=b  --> a=a+b 是先将 a+b 会生成一个新的列表然后重新赋值到 a
# print("未拼接前a 和 b的列表元数据为: ")
# print(a)
# print(b)
# a+=b
# print("拼接后a 和 b的列表元数据为: ")
# print(a)
# print(b)

#切片
# print(f"原始数据:")
# print(a)
#两个冒号后的数字表示步长的意思
# print(a[::1])
# print(a[0:1])  # 切片的数据[beg:end] -->[beg:end)
# print(a[:-1])  # 这里-1表示最后一个元素的下标 len(a)-1
# print(a[len(a)-1])

#切片中指定的步长可以是负数，此时会根据步长从后向前遍历
#若遍历到最后，最后一次步长超过数组的长度时，程序不会报错，会尽可能的遍历到所有的元素
# print(a[::-1])
# print(a[::-2])
# print(a[::-3])
# range (beg,end) --->可以取值 [beg:end)
# for i in range (0,len(a)):
#     print(a[i])
#
# for elem in a:
#     print(elem)




