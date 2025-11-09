# 测试方法的前置和后置操作
class testCase02:
    def setup_method(self):
        print("Setup: Before each test")

    def teardown_method(self):
        print("Teardown: After each test")

    def testCase1(self):
        print("打印第一个用例")