# 循环案例1--计算1到100的和
sum=0
num=1
while num<=100:
    sum+=num
    num+=1
print(f"1到100的和为: {sum}")

# 计算5的阶乘 5！
sum=1
num=1
while num<=5:
    sum*=num
    num+=1
print(f"计算5的阶乘结果为: {sum}")

# 求1！＋2！＋3！＋4！＋5！
num=1
result=0
while num<=5:
    cur = 1
    sum = 1
    while cur<=num:
        sum*=cur
        cur+=1
    num+=1
    result+=sum
print(f"求出的从1的阶乘到5的阶乘的和的值为: {result}")