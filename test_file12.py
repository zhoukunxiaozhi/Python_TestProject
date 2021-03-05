import pytest
import yaml

class TestDemo():
     # @pytest.mark.parametrize(["a","b"],yaml.safe_load(open("./data.yaml")))
     # def test_data(self,a,b):
     #      print(a + b)

     @pytest.mark.parametrize("env", yaml.safe_load(open("./data.yaml")))
     def test_demo(self,env):
          if "test" in env:
               print("测试环境IP：",env["test"])
               print(env)
          elif "dev" in env:
               print("开发环境IP：",env["dev"])
               print(env)
          else:
               print("这TM什么鬼？")

     def test_yaml(self):
          print(yaml.safe_load(open("./data.yaml")))