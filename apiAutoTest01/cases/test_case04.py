# 测试断言操作
import requests


class testCase04:
    # 对接口返回值进行断言操作--抽奖系统活动列表页接口断言操作---返回值为json格式
    # url
        url="http://8.147.235.67:8080/activity/find-list"
    # 请求参数---使用requests时会自动进行参数的拼接
        param={
            "currentPage":1,
            "pageSize":10
        }
    # 需要在请求头中加入token的信息
    # token字段值可以是放在cookie中的，也可以新起的字段名，放入新的字段中
        user_token={
            "User_token":"eyJhbGciOiJIUzI1NiJ9.eyJpZGVudGl0eSI6IkFETUlOIiwiaWQiOjY0LCJpYXQiOjE3NjI2NzMxNTcsImV4cCI6MTc2MjY3Njc1N30.HkoyR99-Pil8WIvXqgtR_N4V8efpAhJ1Gcu9aWNPAnc"
        }
        def tes1t_01(self):
            # 确定请求方法、参数、url
            result = requests.get(self.url, params=self.param, headers=self.user_token)
            # 对响应结果进行断言操作
            print(result.json())
            print(f"响应状态码为：{result.status_code}")
            assert result.json()['data']['total'] == 20

            # 对接口返回值进行断言，返回为 html
            url = "http://jsonplaceholder.typicode.com/"
            expect_text = "Use your own data"
            actual_text = requests.get(url)  # 这里返回的页面信息为html
            assert expect_text in actual_text.text  # 当返回页面信息为 html 时，判断期望的数据是否在实际返回的数据中即可

#断言整数
    # a=1
    # b=2
    # assert a==b,"条件错误a不等于b"

    # 断言字符串--python中字符串是否相等可以直接通过 = 来进行判断
    # str1="abcdef"
    # str2="abcdef"
    # assert str1==str2,"字符串不相等"

    #断言浮点型
    # num1=3.14
    # num2=3.15
    # assert num1>num2,"判断错误"

    # 数据结构断言---判断数据结构是否相等也可以直接使用等号来进行判断
    # 断言列表
    # list1=[1,2,3,"hello"]
    # list2=[2,3,4,"hello"]
    # assert list1==list2

    # 断言元组
    # tuple1=(1,2,3,4,"world")
    # tuple2=(1,2,3,4,"world")
    # assert tuple1==tuple2

    # # 断言字典
    # dict1={"key1":"value1","key2":"value2"}
    # dict2={"key1":"value1","key2":"value2"}
    # assert dict1==dict2

    # 断言集合---常见数据结构的断言操作，判断是否相等均可以直接使用=来进行判读即可
    # set1={1,2,3,4}
    # set2={1,2,3,4}
    # assert set1==set2

    # 断言函数
    # def devide(a,b):
    #     # 断言失败会抛出异常 AssertionError
    #     assert b!=0,"除数为0！出现异常"
    #     return a/b
    #
    #
    # print(devide(10,2)) #正常情况
    # print(devide(10,0)) #异常情况



