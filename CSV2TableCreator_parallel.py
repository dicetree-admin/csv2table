# -*- coding: utf-8 -*-
#!/usr/bin/env  python3

import re
import csv
import time
import os
import sys

import multiprocessing



def regDataType(str):
    str=str.strip()
    if len(str) == 0: return 'BLANK'

    datePattern = """^([1-9]|[0][1-9]|[1][0-2])(\/|-|\.)([1-9]|[0][1-9]|[1-2][0-9]|[3][0-1])(\/|-|\.)[1-2][0-9]{3}|^([1-9]|[0][1-9]|[1-2][0-9]|[3][0-1])(\/|-|\.)([1-9]|[0][1-9]|[1][0-2])(\/|-|\.)[1-2][0-9]{3}|^([1-9]|[0][1-9]|[1-2][0-9]|[3][0-1])(\/|-|\.)(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(\/|-|\.)[1-2][0-9]{3}|^(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(\/|-|\.)([1-9]|[0][1-9]|[1-2][0-9]|[3][0-1])(\/|-|\.)[1-2][0-9]{3}|^[1-2][0-9]{3}(\/|-|\.)([0][1-9]|[1][1-2])(\/|-|\.)([0][1-9]|[1-2][0-9]|[3][0-1])|^[1-2][0-9]{3}([0][1-9]|[1][0-2])([0][1-9]|[1-2][0-9]|[3][0-1])"""

    datetimePattern = """^([1-2][0-9]{3})(\/|-|\.)([0][1-9]|[1][1-2])(\/|-|\.)([0][1-9]|[1-2][0-9]|[3][0-1])[ ]([0-2][0-9])[\:]([0-5][0-9])[\:]([0-5][0-9])|^([1-2][0-9]{3})([0][1-9]|[1][0-2])([0][1-9]|[1-2][0-9]|[3][0-1])([0-2][0-9])([0-5][0-9])([0-5][0-9])$"""

    datetime3Pattern = """^([1-2][0-9]{3})(\/|-|\.)([0][1-9]|[1][1-2])(\/|-|\.)([0][1-9]|[1-2][0-9]|[3][0-1])[ ]([0-2][0-9])[\:]([0-5][0-9])[\:]([0-5][0-9])[\.][0-9]{3}|^([1-2][0-9]{3})([0][1-9]|[1][0-2])([0][1-9]|[1-2][0-9]|[3][0-1])([0-2][0-9])([0-5][0-9])([0-5][0-9])([0-9]{3})$"""

    datetime6Pattern = """^([1-2][0-9]{3})(\/|-|\.)([0][1-9]|[1][1-2])(\/|-|\.)([0][1-9]|[1-2][0-9]|[3][0-1])[ ]([0-2][0-9])[\:]([0-5][0-9])[\:]([0-5][0-9])[\.][0-9]{6}|^([1-2][0-9]{3})([0][1-9]|[1][0-2])([0][1-9]|[1-2][0-9]|[3][0-1])([0-2][0-9])([0-5][0-9])([0-5][0-9])([0-9]{6})$"""

    timePattern = """([0-2][0-9])[\:]([0-5][0-9])[\:]([0-5][0-9])"""

    # intPattern = """^([1-9][0-9]+)$|^(([1-9].*|[1-9][0-9].*)[,].*[0-9]+)$"""
    accountPattern = """^(([1-9].*|[1-9][0-9].*)[,].*[0-9]+)$"""

    """
    bigint  -2^63 (-9,223,372,036,854,775,808) to 2^63-1 (9,223,372,036,854,775,807)    8 Bytes
    int -2^31 (-2,147,483,648) to 2^31-1 (2,147,483,647)    4 Bytes
    smallint    -2^15 (-32,768) to 2^15-1 (32,767)  2 Bytes
    tinyint 0 to 255    1 Byte
    """


    if re.match(datetime6Pattern, str):
        return 'DATETIME(6)'
    if re.match(datetime3Pattern, str):
        return 'DATETIME(3)'
    if re.match(datetimePattern, str):
        return 'DATETIME'
    if re.match(datePattern, str):
        return 'DATE'
    if re.match(timePattern, str):
        return 'TIME'

    if re.match(r'True$|^False$|^0$|^1$', str):
        return 'BIT'
    if re.match(datePattern, str):
        return 'DATE'
    if re.match(accountPattern, str):
        return 'INT'
    if re.match(r'([-+]\s*)?\d+[lL]?$', str):
        return 'INT'
    if re.match(r'([-+]\s*)?[1-9][0-9]*\.?[0-9]*([Ee][+-]?[0-9]+)?$', str):
        return 'FLOAT'
    if re.match(r'([-+]\s*)?[0-9]*\.?[0-9][0-9]*([Ee][+-]?[0-9]+)?$', str):
        return 'FLOAT'
    return 'VARCHAR'


# csv 데이터 check 및 타입확인
def DataTypeFunc(file_path, testRowNum=99999999999):
    rownum = 1

    headerList = []
    valueList = []
    lengthList = []

    totalCnt = sum(1 for line in open(file_path))

    with open(file_path, 'r') as f:
        for row in csv.reader(f, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True):
            try:
                if rownum == 1 :
                    for r in row:
                        r = r.strip().replace(' ','_')
                        headerList.append(r)
                        lengthList.append(['',0,0])
                    rownum += 1
                elif rownum == 2 :
                    for r in row:
                        valueList.append([regDataType(r), r])
                    rownum += 1

                elif rownum >= testRowNum:
                    print('ww')
                    break
                else:
                    for r in range(len(row)):
                        if lengthList[r][1] < len(row[r]):
                            lengthList[r][0] = row[r]
                            lengthList[r][1] = len(row[r])
                    rownum += 1

                if rownum % 10000 == 0:
                    progress(rownum, totalCnt, start_time)


            except Exception as e:
                print('error Msg : ' , e)
                break

    rowCount = rownum - 1

    DataTypeList = []
    for k in range(len(headerList)):
        DataTypeList.append([headerList[k], valueList[k][0], valueList[k][1], lengthList[k][0], lengthList[k][1] ])


    return DataTypeList, rowCount




# table create script
def scriptCreator(file_path):
    dataTypeList = DataTypeFunc(file_path)

    for row in dataTypeList:
        print(row)

    DDLscript = ''

    return DDLscript




def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0




def progress(count, total, start_time, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    now_time = time.time()
    elapsed_time = int(now_time - start_time)

    sys.stdout.write('[%s] %s%s, %d sec...%s\r' % (bar, percents, '%', elapsed_time, status))
    sys.stdout.flush()



def printResult(file_path, start_time):
    # DataTypeList = DataTypeFunc(file_path, testRowNum)
    DataTypeList, rowCount = DataTypeFunc(file_path)

    headerLine = [['COLUMN_NAME','PREDICT_DATA_TYPE', '1ST_ROW_VALUE', 'MAX_LENGTH_ROW_VALUE', 'MAX_LENGTH' ]]
    borderLine = [['-------------','-------------','-------------','-------------','-------------']]
    printList = headerLine + borderLine + DataTypeList
    print('\n\n')
    for row in printList:
        line = ''
        for i in range(len(row)):
            if len(str(row[i])) < 28:
                line += str(row[i]) + ' '*(30 - len(str(row[i])))
            else:
                line += str(row[i])[:26] + '..  '
        print(line)

    end_time = time.time()

    elapsedTime = end_time - start_time

    file_size_bytes = os.path.getsize(file_path)
    file_size_conv = str(convert_bytes(file_size_bytes))

    print('--'*20)
    print('File size : %s \nrow(s) : %d \nElapsed Time : %f sec' % (file_size_conv, rowCount, elapsedTime))



if __name__=="__main__":

    # file_path = '100 Sales Records.csv'
    file_path = '1500000 Sales Records.csv'
    start_time = time.time()
    # testRowNum = 4
    pool = multiprocessing.Pool(processes=2)
    pool.map(printResult(file_path, start_time))
    pool.close()
    pool.join()



""" 
File size : 178.5 MB 
row(s) : 1500001 
Elapsed Time : 9.219732 sec
"""
