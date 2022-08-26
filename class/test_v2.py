
#在类内分组测试时需要注意的是，每个测试都有一个类的唯一实例。
#让每个测试共享同一个类实例将对测试隔离非常有害，并会促进不良的测试实践

class TestClassDemoInstance:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 1

    #在测试函数签名中列出名称tmp_path，pytest将在执行测试函数调用之前查找并调用fixture工厂来创建资源。
    #在测试运行之前，pytest创建一个唯一的每次测试调用临时目录
    def test_needsfiles(tmp_path):
        print(tmp_path)
        assert 0