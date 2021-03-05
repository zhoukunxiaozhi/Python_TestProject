
e = open('test_file1.py','rt')
# print(e.read())
# print(e.readline())
# print(e.readline())
# print(e.readline())
print(e.readlines())
# print(e.readable())
e.close()

with open('test_file1.py','rt') as f:
    # print(f.readlines())
    while True:
        line = f.readline()
        if line:
            print(line)
        else:
            break


import json
info=[{
     "name":"Tom",
     "age":13,
     "sex":"Male"
      },{
     "name": "Jerry",
     "age": 12,
     "sex": "Female"
     }]

data1 = json.dumps(info,sort_keys=True,indent=2)
print(data1)
print(type(data1))

print("写入数据到test_file中")
json.dump(info, open('test_file', 'w'))

data2 = json.loads(data1)
print(data2)
print(type(data2))
print(data2[0]['name'])

data3 = json.load(open('test_file', 'r'))
print(data3)
print(type(data3))
print(data3[1]['sex'])
