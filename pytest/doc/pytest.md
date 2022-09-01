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

## 3 其他

```python

#pytest将重写的模块写回磁盘以进行缓存。
#您可以通过将其添加到conftest的顶部来禁用此行为（例如，避免在大量移动文件的项目中留下过时的.pyc文件）。

import sys
sys.dont_write_bytecode = True
```
