# 对字典进行操作
from operator import contains
# 定义一个空的字典对象
# container=dict()

container={
    "id":1,
    "name":"zhangsan",
    "age":18
}
# print(container)

# 可以对字典进行读操作，也可以对字典进行写操作
# 对字典的操作都是对 key 的操控

#新增元素
container["score"]=40
# print(container)

#遍历字典
# for key in container:
#     print(f"键key的值为: {key},所对应的value值是: {container[key]}")

#获取所有key
# print("打印所有 key 的信息:",end=" ")
# for elem in container.keys():
#     print(elem,end=" ")
#获取所有的value
# print("\n打印所有的 value 的信息:,",end=" ")
# for elem in container.values():
#     print(elem,end=" ")
# 获取所有的键值对
# print("\n对应所有 key-value 的信息:",end=" ")
# for elem in container.items():
#     print(elem,end=",")

print(container)
#删除元素
container.pop("id")

print(container)


#由于列表和字典是可变的，因此列表和字典不可以作为可哈希类型
#可哈希类型==可作为key，key应该是唯一的，是不可变的，一个不可变的对象一般为可哈希的。可变的，一般就是不可哈希的
# 字典、列表、元组，它们内部可以再包含其他元素，这些可以包含其他元素的类型的类型又可以称之为容器/集合类
