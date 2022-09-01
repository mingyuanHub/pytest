# pytest

## 1 安装 `pytest`

`pip install -U pytest`

## 2 命令

 ```python

#帮助文档
pytest -h

#查看版本号
pytest -V

#运行测试
pytest test_v1.py

#运行文件夹下所有测试
pytest ./
pytest ./tp

#运行指定测试
pytest test_mod.py::TestClass::test_method

#支持print输出 -s
pytest ./ -s

#将运行所有用@pytest.mark修饰的测试
pytest -m slow

#要获取超过1.0秒的最慢10个测试持续时间列表：
pytest --durations=10 --durations-min=1.0

#您可以使用-p选项在命令行中显式地早期加载插件（内部和外部）：
pytest -p mypluginmodule

#要禁用在调用时加载特定插件，请使用-p选项和前缀no:。
pytest -p no:doctest

#您可以从命令行通过Python解释器调用测试：
python -m pytest [...]

#通过实现pytest_assertrepr_compare钩子，可以添加您自己的详细解释。
pytest_assertrepr_compare

 ```

## 3 pytest 前置与后置

```text
模块级别：setup_module、teardown_module

函数级别：setup_function、teardown_function，不在类中的方法

类级别：setup_class、teardown_class

方法级别：setup_method、teardown_method

方法细化级别：setup、teardown
```

## 4 pytest fixture

> https://zhuanlan.zhihu.com/p/87775743?from_voters_page=true

### 4.1  `fixture`可以在一个类、或者一个模块、或者整个session中被共享
```python
#如果想在一个模块中使用，那么
@pytest.fixture(scope="module")

#如果想在一个类中使用，那么
@pytest.fixture(scope="class")

#如果想在全部会话中使用，那么
@pytest.fixture(scope="session")
```

## 5 pytest mark.parametrize()

`@pytest.mark.parametrize()`

* 数据驱动 ：其实就是把我们测试用例的数据放到excel，yaml，csv，mysql，然后通过去改变数据达到改变测试用例的执行结果 。
* @pytest.mark.parametrize(args_name,args_value)
* args_name：参数名，字符串，多个参数中间用逗号隔开
* args_value：参数值（列表，元组，字典列表，字典元组），有多个值用例就会执行多少次，是list,多组数据用元祖类型;传三个或更多参数也是这样传。list的每个元素都是一个元组，元组里的每个元素和按参数顺序一一对应

```python
import pytest

@pytest.mark.parametrize('a', [1, 2, 3])
@pytest.mark.parametrize('b', [2, 3, 4])
def test_data(a, b):
    print(a, b)

# 执行9次测试
```

## 6 pytest pytestconfig
> https://www.cnblogs.com/guanqibuyu/p/16579280.html

```python
# 从配置对象获取 cmdopt 的值
@pytest.fixture(scope='session')
def cmdopt(pytestconfig):
    input_arg = pytestconfig.getoption('--cmdopt')
    print('input_arg', input_arg)
    return input_arg
```

## 7 pytest request

> https://www.bilibili.com/read/cv12424194

## 其他

```python

#pytest将重写的模块写回磁盘以进行缓存。
#您可以通过将其添加到conftest的顶部来禁用此行为（例如，避免在大量移动文件的项目中留下过时的.pyc文件）。

import sys
sys.dont_write_bytecode = True
```
