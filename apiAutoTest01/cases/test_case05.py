# 参数化的测试--参数化可以是针对类的也可以是针对函数的
import pytest


# 针对类中所有函数进行参数化---case3、case4
# @pytest.mark.parametrize("expect_input,actual_data",[(2,3),(1,2)])
# class TestCase05:
    # 针对函数进行参数化--单个变量
    # @pytest.mark.parametrize("num",[1,2,3,4])
    # def testCase1(self,num):
    #     print(num)

    # 针对函数进行参数化--多个变量
    # @pytest.mark.parametrize("expect_input,actual_data",[("3+5",8),("2+4",6)])
    # def testCase2(self,expect_input,actual_data):
    #     assert eval(expect_input)==actual_data

    # def testCase3(self,expect_input,actual_data):
    #     assert expect_input*1+1 == actual_data
    #
    # def testCase4(self,expect_input,actual_data):
    #     assert expect_input+1 == actual_data

    # 想要对模块中所有测试参数化，可以使用全局 pytestmark ，注意全局变量的名称必须为这个
    # pytestmark = pytest.mark.parametrize("expect_input,actual_data",[(2,3),(1,2)])
    # def testCase3(self,expect_input,actual_data):
    #     assert expect_input*1+1 == actual_data

    # 自定义参数化数据源
    # @staticmethod
    # def sourceData():
    #     return [1,2,3,4]
    #
    # @pytest.mark.parametrize("num",sourceData())
    # def testCase5(self,num):
    #     print(num)
