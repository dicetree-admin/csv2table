#!/usr/bin/env  python3

# import csv
# data = []
# # with open('100 Sales Records.csv',  'r') as f:
# with open('1500000 Sales Records.csv',  'r') as f:
#     for index, row in enumerate(csv.DictReader(f, delimiter=',')):
#         if index >= 1:
#             break
#         else:
#             print(row.keys())
#         print(row)
    # reader = csv.DictReader(f, delimiter=',')
    # print(type(reader))
    # for line in reader:
    #     line['Price'] = float(line['Price'])
    #     data.append(line)


# import pandas as pd
# df = pd.read_csv('100 Sales Records.csv')
# print(type(df))

# filename = '100 Sales Records.csv'

# import csv
# with open(filename, "r") as csvfile:
#     datareader = csv.reader(csvfile)
#     count = 0
#     for row in datareader:
#         if row[3] in ("column header", 'a'):
#             # doSomething(row)
#             count += 1
#         elif count > 2:
#             break

# import dask.dataframe as dd
# filename = '100 Sales Records.csv'
# df = dd.read_csv(filename, dtype='str')
# print(df)


# import csv
# import collections
#
# filename = '100 Sales Records.csv'
# with open(filename,'rb') as f:
#     r = csv.reader(f)
#     od = collections.OrderedDict(r)
# print(od)



# filename = '100 Sales Records.csv'
# f = open(filename, 'r')
# lines = f.readlines()
# # i = 0
# # while i > 2:
# #     for line in lines:
# #         print(line)
# #     i += 1
#
# for i in range(0,2):
#     f.read(i)
#
# f.close()


# import ast, re
# def dataType(str):
#     str=str.strip()
#     if len(str) == 0: return 'BLANK'
#     try:
#         t=ast.literal_eval(str)
#
#     except ValueError:
#         return 'TEXT'
#     except SyntaxError:
#         return 'TEXT'
#
#     else:
#         if type(t) in [int, float, bool]:
#             if t in set((True,False)):
#                 return 'BIT'
#             if type(t) is int:
#                 return 'INT'
#             if type(t) is float:
#                 return 'FLOAT'
#         else:
#             return 'TEXT'
#
#
# def regDataType(str):
#     str=str.strip()
#     if len(str) == 0: return 'BLANK'
#
#     datePattern = """^([1-9]|[0][1-9]|[1][0-2])(\/|-|\.)([1-9]|[0][1-9]|[1-2][0-9]|[3][0-1])(\/|-|\.)[1-2][0-9]{3}|
# ^([1-9]|[0][1-9]|[1-2][0-9]|[3][0-1])(\/|-|\.)([1-9]|[0][1-9]|[1][0-2])(\/|-|\.)[1-2][0-9]{3}|
# ^([1-9]|[0][1-9]|[1-2][0-9]|[3][0-1])(\/|-|\.)(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(\/|-|\.)[1-2][0-9]{3}|
# ^(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(\/|-|\.)([1-9]|[0][1-9]|[1-2][0-9]|[3][0-1])(\/|-|\.)[1-2][0-9]{3}|
# ^[1-2][0-9]{3}(\/|-|\.)([0][1-9]|[1][1-2])(\/|-|\.)([0][1-9]|[1-2][0-9]|[3][0-1])|
# ^[1-2][0-9]{3}([0][1-9]|[1][0-2])([0][1-9]|[1-2][0-9]|[3][0-1])"""
#
#     datetimePattern = """^([1-2][0-9]{3})(\/|-|\.)([0][1-9]|[1][1-2])(\/|-|\.)([0][1-9]|[1-2][0-9]|[3][0-1])[ ]([0-2][0-9])[\:]([0-5][0-9])[\:]([0-5][0-9])|^([1-2][0-9]{3})([0][1-9]|[1][0-2])([0][1-9]|[1-2][0-9]|[3][0-1])([0-2][0-9])([0-5][0-9])([0-5][0-9])$"""
#
#     datetime3Pattern = """^([1-2][0-9]{3})(\/|-|\.)([0][1-9]|[1][1-2])(\/|-|\.)([0][1-9]|[1-2][0-9]|[3][0-1])[ ]([0-2][0-9])[\:]([0-5][0-9])[\:]([0-5][0-9])[\.][0-9]{3}|^([1-2][0-9]{3})([0][1-9]|[1][0-2])([0][1-9]|[1-2][0-9]|[3][0-1])([0-2][0-9])([0-5][0-9])([0-5][0-9])([0-9]{3})$"""
#
#     datetime6Pattern = """^([1-2][0-9]{3})(\/|-|\.)([0][1-9]|[1][1-2])(\/|-|\.)([0][1-9]|[1-2][0-9]|[3][0-1])[ ]([0-2][0-9])[\:]([0-5][0-9])[\:]([0-5][0-9])[\.][0-9]{6}|^([1-2][0-9]{3})([0][1-9]|[1][0-2])([0][1-9]|[1-2][0-9]|[3][0-1])([0-2][0-9])([0-5][0-9])([0-5][0-9])([0-9]{6})$"""
#
#
#     if re.match(datetime6Pattern, str):
#         return 'DATETIME(6)'
#     if re.match(datetime3Pattern, str):
#         return 'DATETIME(3)'
#     if re.match(datetimePattern, str):
#         return 'DATETIME'
#     if re.match(datePattern, str):
#         return 'DATE'
#
#     if re.match(r'True$|^False$|^0$|^1$', str):
#         return 'BIT'
#     if re.match(r'([-+]\s*)?\d+[lL]?$', str):
#         return 'INT'
#     if re.match(r'([-+]\s*)?[1-9][0-9]*\.?[0-9]*([Ee][+-]?[0-9]+)?$', str):
#         return 'FLOAT'
#     if re.match(r'([-+]\s*)?[0-9]*\.?[0-9][0-9]*([Ee][+-]?[0-9]+)?$', str):
#         return 'FLOAT'
#
#
#     return 'TEXT'
#
#
#
# inFile = '100 Sales Records.csv'
# # inFile = '1500000 Sales Records.csv'
# fr = open(inFile, 'r', newline='')
# # header = fr.readline().strip()
# # header_list = header.split(',')  # 문자열 --> 리스트
# # header_str = ','.join( map(str,header_list)) # 리스트 --> 문자열
# # print(header_str)
# i = 0
# for  row in fr :
#     if i < 2:
#         row = row.strip()
#         row_list = row.split(',')
#         for row2 in row_list:
#             print(row2, regDataType(row2))
#         # row_str = ','.join( map(str, row_list))
#         # print(row_str)
#         i += 1
#     else:
#         break
# fr.close()
#
#
#
#
#
#
# def dataTypeFunc(file_path):
#
#     headerList = []
#     valueList = []
#     fr = open(file_path, 'r', newline='')
#     i = 0
#     for  row in fr :
#         if i == 0:
#             row = row.lstrip().rstrip().replace(' ','_').upper()
#             row_list = row.split(',')
#             for row2 in row_list:
#                 # print(row2, regDataType(row2))
#                 headerList.append([row2, regDataType(row2)])
#             i += 1
#         elif i == 1:
#             row = row.strip()
#             row_list = row.split(',')
#             for row2 in row_list:
#                 # print(row2, regDataType(row2))
#                 valueList.append([row2, regDataType(row2)])
#             i += 1
#         else:
#             break
#     fr.close()
#
#     dataTypeList = [headerList, valueList]
#
#     return dataTypeList


# testTxt = '''Australia and Oceania,Tuvalu,Baby ,"A ,B",Food,Offline," Has","mar,28/2010","6691,65933",6/27/2010,9925,255.28,159.42,2533654,1582243.5,951410.5," 1,582,244 "'''
# textTxt = '''Australia and Oceania,"Baby,Food",2533654,1582243.5,951410.5,"1,582,244"'''
textTxt = '''Food,abc,"Tu""v""alu,100",Australia,"Oce,ania","Baby,Food",9510.5,"1,582,244"'''
# tmpList = testTxt.split(',"')
# print(tmpList)
# import re
# # ★
# textTxt = re.sub('[\,][\"]','★',textTxt)
# textTxt = re.sub('[\"][\,]','★',textTxt)
#
# print(textTxt)
#
# textList = textTxt.split('★')
#
# for row in textList:
#     print(row)

import csv

file_path = '100 Sales Records.csv'
lines = '''"AAA", "BBB", "Test, Test", "CCC"
           "111", "222, 333", "XXX", "YYY, ZZZ"'''.splitlines()
with open(file_path,  'r') as f:
    i = 0
    for row in  csv.reader(f, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True):
        if i < 2:
            print(row)
            i += 1
        else:
            break

# with open('100 Sales Records.csv',  'r') as f:
# with open(file_path,  'r') as f:
#     for index, row in enumerate(csv.DictReader(f, delimiter=',')):
#         if index >= 1:
#             break
#         else:
#             print(row.keys())
#         print(row)