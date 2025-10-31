# 输入一个整数，判定是奇数还是偶数
# num = input("请输入一个整数: ")
# # 转化为整数
# num = int(num)
# 2和4行代码可以整合为一行代码，用 num=int(input("请输入一个整数："))
# # 判断
# if num % 2 == 0:
#     print("偶数")
# else:
#     print("奇数")

# 输入一个整数，判断是整数还是负数
# num=input("请输入一个整数: ")
# num=int(num)
# if num<0 :
#     print("负数")
# elif num>0 :
#     print("正数")
# else:
#     print("为0")



# 判断年份是否为闰年，闰年：每4年闰一次，还有个特例是世纪闰年，年份能够被100整除，eg：1900
# year=input("请输入一个年份: ")
# year=int(year)
# 将上面两行代码整合为以下代码
year=int(input("请输入一个年份: "))
if year%100==0:
    # 判定世纪闰年
    if year%400==0:
        print("闰年")
    else:
        print("平年")
else :
 # 判定普通闰年
    if year%4==0:
        print("闰年")
    else :
        print("平年")

# 判定是否为闰年的要求是，年份%400为0是闰年。年份%4为0并且年份%100不为0，为闰年
num=input("请输入一个年份: ")
num=int(num)
if(num%100!=0 and num%4==0) or num%400==0 :
    print("闰年")
else :
    print("平年")


