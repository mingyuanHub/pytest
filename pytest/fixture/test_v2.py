import pytest
import os

# http://www.wjhsh.net/breakcircle-p-13099493.html
# fixture里面有个参数autouse，默认是Fasle没开启的，；
# 如果设置为True开启自动使用fixture功能，每个用例执行前都会调用, 这样用例就不用每次都去传参了
# 如果设置为False开启自动使用fixture功能，用例 @pytest.mark.usefixtures("get_status") 才会调用


@pytest.fixture(scope="function", autouse=False)
def get_status():
    case_name = os.path.basename(os.path.abspath(__file__)).replace(".py", "")
    print(case_name + " begin")
    yield 1 if case_name.isalnum() else 0
    print(case_name + " finish")


@pytest.mark.usefixtures("get_status")
def test_1():
    print(1111)


def test_name():
    print(2222)

# test_v2 begin
# 1111
# .test_v2 finish
# 2222