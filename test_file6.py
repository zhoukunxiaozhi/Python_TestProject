"""
import os
# os.mkdir("testdir")
# os.removedirs("testdir")
# print(os.listdir("./"))
# print(os.getcwd())

print(os.path.exists("X"))
if not os.path.exists("X"):
    os.mkdir("X")
print(os.path.exists("X/test.txt"))
# if not os.path.exists("X/test.txt"):
with open('X/test.txt', 'w') as f:
    f.write("Hello,World!")
    f.closed
"""

# import time
# print(time.asctime())
# print(time.time())
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

"""
now_time = time.time()
want_time_1 = now_time - 2*24*60*60
want_time_2 = time.localtime(want_time_1)
print(time.strftime("%Y-%m-%d %H:%M:%S", want_time_2))
"""


import urllib.request
response:object=urllib.request.urlopen('http://www.baidu.com')
print(response.status)
# print(response.read())
print(response.headers)


# import math
# print(math.ceil(5.3))
# print(math.floor(5.9))
# print(math.sqrt(16))