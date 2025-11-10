# fixture 中通过 params 可以实现参数化
import pytest

# 定义一个参数化的 fixture
# @pytest.fixture(params=["a","b"])
# def data_provide(request):
#     return request.param

# 定义参数化的 fixture---会依次读取可迭代的对象，每次读取可迭代对象中的一个值
@pytest.fixture(params=[
    {"name":"zhangsan","age":20},
    {"name":"lisi","age":18}
])
def data_provide(request):
    return request.param

# 定义一个测试函数，它依赖于上面的参数化 fixture
def est_data(data_provide):
    assert data_provide != None
    assert data_provide["age"]>=18  # 字典针对 key 来进行操作
    print(f"Testing with data provider:{data_provide}")