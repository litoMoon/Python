# 输入四个整数/小数，求四个小数的平均值
num1 = input("请输入第一个数字：")
num2 = input("请输入第二个数字：")
num3 = input("请输入第三个数字：")
num4 = input("请输入第四个整数：")

# 类型转换
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
num4 = int(num4)

# 求和算平均值
average=(num1+num2+num3+num4)/4
# 输出平均值
print(f"平均值为: {average}")
