# import pytest
#
# def test_success():
#      assert True
#
# def test_failure():
#      assert False
#
# def test_skip():
#      pytest.skip('for a reason!')
#
# def test_broken():
#      raise Exception('oops')


import pytest
import allure

@allure.feature("登录模块")
class Testlogin():
     @allure.severity(allure.severity_level.TRIVIAL)
     @allure.story("登录成功")
     def test_login_a(self):
          print("这是登录测试用例，登录成功")
          pass

     @allure.severity(allure.severity_level.MINOR)
     @allure.story("登录失败")
     def test_login_b(self):
          print("这是登录测试用例，登录失败")
          pass

     @allure.severity(allure.severity_level.NORMAL)
     @allure.story("用户名缺失")
     def test_login_c(self):
          print("用户名缺失")
          pass

     @allure.severity(allure.severity_level.CRITICAL)
     @allure.story("密码缺失")
     def test_login_d(self):
          with allure.step("输入用户名"):
               print("输入用户名")
          with allure.step("输入密码"):
               print("输入密码")
          with allure.step("点击登录"):
               print("点击登录")
          print("密码缺失")
          pass

     TEST_CASE_LINK = "https://www.baidu.com/"
     @allure.severity(allure.severity_level.BLOCKER)
     @allure.testcase(TEST_CASE_LINK,"登录用例")
     @allure.link("https://www.baidu.com/",name="百度首页")
     # --allure-link-pattern=issue:https://www.baidu.com/issue/{}
     @allure.issue('100','BUG清单')
     @allure.story("链接功能")
     def test_with_link(self):
          print("这是一条加了链接的测试")
          pass

     def test_attach_text(self):
          allure.attach("这是一个纯文本信息",attachment_type=allure.attachment_type.TEXT)

     def test_attach_html(self):
          allure.attach("<body>HTML代码块</body>","HTML测试",attachment_type=allure.attachment_type.HTML)

     def test_attach_photo(self):
          allure.attach.file("C:/Users/Zhoukun/Pictures/Saved Pictures/111.jpg","图片",attachment_type=allure.attachment_type.JPG)

if __name__ == '__main__':
     pytest.main()