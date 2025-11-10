#测试 fixture----可以将函数名作为参数进⾏调⽤
import pytest

class testFixture:
    # @pytest.fixture
    # def case1(self):
    #     return [1,2,3,4,5]
    #
    # def testCase1(self,case1):
    #     print(case1)

    # fixture的嵌套使用
    # @pytest.fixture
    # def case1(self):
    #     print("case1")
    #
    # @pytest.fixture
    # def case2(self,case1):
    #     print("case2")
    #
    # @pytest.fixture
    # def case3(self,case2):
    #     print("case3")
    #
    # def testCase2(self,case3):
    #     print("测试完毕，输出结果应依次为case1、case2、case3")


    # 在文件操作中使用fixture---读文件
    @pytest.fixture
    def beforeOperator1(self):
        fo = open("test.txt", "r",encoding="utf-8")

        yield fo

        print("文件读取操作完成关闭文件")
        fo.close()

    # 在文件操作中使用fixture---写文件
    @pytest.fixture
    def beforeOperator2(self):
        print("文件操作前打开文件:")
        fo = open("test.txt", "w",encoding="utf-8")

        yield fo

        print("文件写入操作完成关闭文件")
        fo.close()


    # def testCase3(self,beforeOperator):
    #     print(beforeOperator.read())

    # def testCase4(self,beforeOperator):
    #     data="一定要相信自己"
    #     print(data)
    #     print(beforeOperator.write("一定要相信自己"))

    # 针对文件进行先写后读操作
    # def testCase5(self,beforeOperator2,beforeOperator1):
    #     beforeOperator2.write("一定要相信自己")
    #     print("文件写取操作完成关闭文件")
    #     beforeOperator2.close()
    #     print("正在执行读取文件操作，读取到的数据为: ", end="")
    #     print(beforeOperator1.read())

    # 这两者是不同的句柄 beforeOperator2，beforeOperator1
    def testCase6(self,beforeOperator2,beforeOperator1):
        # 写时是先写入缓冲区内的，若未达到要求需要手动刷新缓冲区
        beforeOperator2.write("一定要相信自己")
        beforeOperator2.flush()
        print("正在执行读取文件操作，读取到的数据为: ", end="")
        print(beforeOperator1.read()) #注意这里句柄切换了，以至于后续执行yield后面内容时，先执行beforeOperator1的而不是beforeOperator2的
