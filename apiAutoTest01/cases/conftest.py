import pytest


@pytest.fixture(scope="session",autouse=True)
def testFixture():
    print("函数执行前初始化操作")

    yield

    print("函数执行完毕后处理操作")