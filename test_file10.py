import pytest
import pytest_assume

def setup_module():
     print("这是个setup_module方法")
def teardown_module():
     print("这是个teardown_module方法")
def setup_function():
     print("这是个setup_function方法")
def teardown_function():
     print("这是个teardown_function方法")

def test_a():
     print("hello")
     pass

class TestDemo1():
     def setup_class(self):
          print("这是个setup_class方法")
     def setup_method(self):
          print("这是个setup_method方法")
     def setup(self):
          print("这是个setup方法")

     def teardown_class(self):
          print("这是个teardown_class方法")
     def teardown_method(self):
          print("这是个teardown_method方法")
     def teardown(self):
          print("这是个teardown方法")

     def test_1(self):
          print("开始执行test_1方法")
          x = "this"
          assert "s" in x

     def test_2(self):
          print("开始执行test_2方法")
          y = "hello"
          assert "c" in y

     def test_3(self):
          print("开始执行test_3方法")
          a = "hello"
          b = "hello world"
          assert a in b

class TestDemo2():
     def test_4(self):
          print("开始执行test_4方法")
          x = "this"
          assert "t" in x
          # pytest.assume("n" in x)
          # pytest.assume("g" in x)
          # pytest.assume(1 == 2)

     def test_5(self):
          print("开始执行test_5方法")
          y = "hello"
          assert "o" in y

     def test_6(self):
          print("开始执行test_6方法")
          a = "hello"
          b = "hello world"
          assert a not in b

if __name__ == '__main__':
     pytest.main()
     # pytest.main(['-v','-x','TestDemo1'])