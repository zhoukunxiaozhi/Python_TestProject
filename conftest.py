import pytest

@pytest.fixture()
def login():
     print("这是个登录方法")

def pytest_configure(config):
     marker_list = ["search","login"]
     for markers in marker_list:
          config.addinivalue_line(
               "markers",markers
          )
