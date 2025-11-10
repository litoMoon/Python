# 测试带参数的fixture
import pytest


# 如果一个方法中只有添加了 fixture 注解的方法,在执行 pytest 时添加该注解的这个方法不会执行
# 这里输入 pytest 时,只有执行了 TestClass 类里的两个方法
# @pytest.fixture(scope="function")
# def testFixture():
#     print("函数执行前初始化操作")
#
#     yield
#
#     print("函数执行完毕后处理操作")
#
# class TestClass:
#     def testCase1(self,testFixture):
#         print("第一个case方法")
#
#     def testCase2(self,testFixture):
#         print("第二个case方法")

# ------------------------------------------------
# 当 scope 设置为类时,不是类中所有方法都会执行 fixture 注解所在的方法,只会在类中所有方法执行的前后执行一次
# @pytest.fixture(scope="class")
# def testFixture():
#     print("函数执行前初始化操作")
#
#     yield
#
#     print("函数执行完毕后处理操作")
#
# class TestClass:
#     def testCase1(self,testFixture):
#         print("第一个case方法")
#
#     def testCase2(self,testFixture):
#         print("第二个case方法")

# -------------------------------------------------
# 当 scope 设置为 module 时,共享 fixture 的范围在当前模块,一个文件中的数据共享这个数据
class testClass1:
    def testCase1(self):
        print("第一个case方法")

    def testCase2(self):
        print("第二个case方法")
class testClass2:
    def testCase1(self):
        print("第一个case方法")

    def testCase2(self):
        print("第二个case方法")