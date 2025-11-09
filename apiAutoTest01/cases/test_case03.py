# 测试类的前置和后置操作，会在当前整个所有符合条件的方法前执行setup，方法后执行teardown
class testCase03:
    def setup_class(self):
        print("class : 满足条件的函数前执行")

    def teardown_class(self):
        print("class : 满足条件的函数后执行")

    def testCase1(self):
        print("这是第一个测试方法")

    def testCase2(self):
        print("这是第二个测试方法")

    def testCase3(self):
        print("这是第三个测试方法")