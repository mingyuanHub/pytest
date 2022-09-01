import pytest


# 注册自定义参数 cmdopt 到配置对象
def pytest_addoption(parser):
    parser.addoption("--cmdopt", action="store",
                     default="None",
                     help="将自定义命令行参数 ’--cmdopt' 添加到 pytest 配置中")

    parser.addoption("--html", action="store",
                     default="None",
                     help="将自定义命令行参数 ’--html' 添加到 pytest 配置中")


# 从配置对象获取 cmdopt 的值
@pytest.fixture(scope='session')
def cmdopt(pytestconfig):
    input_arg = pytestconfig.getoption('--cmdopt')
    ht = pytestconfig.getoption('--html')
    print('input_arg', input_arg)
    print('ht', ht)
    return 1234567