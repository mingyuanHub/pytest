#开发多个测试后，您可能希望将它们分组到一个类中。
# pytest使创建包含多个测试的类变得容易

class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")