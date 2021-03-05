# import requests
# r = requests.get('http://www.baidu.com/')
# r.encoding = "utf-8"
# print(r.status_code)
# print(r.encoding)
# print(r.text)
#
# s = requests.post('https://httpbin.org/post',data={'key':'value'})
# print(s.status_code)
# print(s.encoding)
# print(s.text)

# from openpyxl import Workbook
# from openpyxl.utils import get_column_letter
#
# wb = Workbook()
#
# dest_filename = 'empty_book1.xlsx'
#
# ws1 = wb.active
# ws1.title = "range names"
# for row in range(1, 40):
#      ws1.append(range(600))
#
# ws2 = wb.create_sheet(title="Pi")
# ws2['F5'] = 3.14
#
# ws3 = wb.create_sheet(title="Data")
# for row in range(10, 20):
#     for col in range(27, 54):
#         _= ws3.cell(column=col, row=row, value="{0}".format(get_column_letter(col)))
#
# ws4 = wb.create_sheet(title="My_Sheet")
# for row in range(1, 11):
#     for col in range(1, 11):
#         ws4.cell(column=col, row=row, value="{0}".format(get_column_letter(col)))
#
# wb.save(filename = dest_filename)


# from openpyxl import load_workbook
# wb = load_workbook(filename = 'empty_book1.xlsx')
# sheet_ranges = wb['My_Sheet']
# print(sheet_ranges['E10'].value)
# for i in range(1,11):
#     print(sheet_ranges.cell(column=1, row=i).value)

'''
import json

info1={
     "name":"Tom",
     "age":13,
     "sex":"Male"
     }

info2=["Tom","Jerry"]

info3=[{
     "name":"Tom",
     "age":13,
     "sex":"Male"
      },{
     "name": "Jerry",
     "age": 12,
     "sex": "Female"
     }]

print(info1)
print(type(info1))

data1 = json.dumps(info1,sort_keys=False)
print(data1)
print(type(data1))

print("写入数据到test_file中")
json.dump(info1, open('test_file', 'w'))

data2 = json.loads(data1)
print(data2)
print(type(data2))

data3 = json.load(open('test_file', 'r'))
print(data3)
print(type(data3))
'''

import yaml

f = open('a.yaml', encoding='utf-8')
res = yaml.load(f,Loader=yaml.FullLoader)
print(res)
print(type(res))
f.close()

print(yaml.dump(res))

with open('b.yaml','w') as f:
     yaml.dump(data=res,stream=f)