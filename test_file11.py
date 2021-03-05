'''
import pytest

def test_case1(login):
     print("test_case1,准备登录")
     pass

def test_case2():
     print("test_case2,不用登录")
     pass

def test_case3(login):
     print("test_case3,准备登录")
     pass

if __name__ == '__main__':
     pytest.main()
'''


import pytest

# @pytest.fixture(scope="module")
# def open():
#      print("打开浏览器")
#      yield
#
#      print("执行teardown！")
#      print("关闭浏览器")
#
#
# def test_search1(open):
#      print("test_search1")
#      pass
#
# def test_search2(open):
#      print("test_search2")
#      pass
#
# def test_search3(open):
#      print("test_search3")
#      pass
#
# if __name__ == '__main__':
#      pytest.main()

# @pytest.fixture(autouse=True)
# def open():
#      print("打开浏览器")
#
# def test_search1():
#      print("test_search1")
#      pass
#
# def test_search2():
#      print("test_search2")
#      pass
#
# def test_search3():
#      print("test_search3")
#      pass
#
# if __name__ == '__main__':
#      pytest.main()


# import pytest
#
# @pytest.mark.parametrize("test_input,expected",[("1+2",3),("3+5",8),("5*5",11)])
# def test_eval(test_input,expected):
#      assert eval(test_input) == expected
#
#
# @pytest.mark.parametrize("x",[1,2,3])
# @pytest.mark.parametrize("y",[67,4,325])
# def test_foo(x,y):
#      print(f"测试数据组合x:{x},y:{y}")

# import sys
# import pytest
#
# test_user_data = ['Tom','Jerry']
# @pytest.fixture(scope="module")
# def login_r(request):
#      user=request.param
#      print(f"\n 打开首页准备登录，登录用户：{user}")
#      return user
#
# @pytest.mark.xfail
# # @pytest.mark.skip(sys.platform == 'win32',reason="不在Windows平台执行")
# @pytest.mark.parametrize("login_r",test_user_data,indirect=True)
# def test_login(login_r):
#      a = login_r
#      print(f"测试用例中的返回值;{a}")
#      assert a !=""
#      raise NameError


@pytest.mark.search
def test_search1():
     print("test_search1")
     pass

@pytest.mark.search
def test_search2():
     print("test_search2")
     pass

@pytest.mark.search
@pytest.mark.xfail
def test_search3():
     print("test_search3")
     raise NameError

@pytest.mark.login
def test_login1():
     print("test_login1")
     pass

@pytest.mark.login
def test_login2():
     print("test_login2")
     pass

if __name__ == '__main__':
     pytest.main()