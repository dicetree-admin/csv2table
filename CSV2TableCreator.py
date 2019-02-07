# -*- coding: utf-8 -*-
#!/usr/bin/env  python3

import re
import csv
import time
import os
import sys


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




def progress(rownum, total_file_cnt, file_cnt, totalCnt, start_time, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * rownum / float(totalCnt)))

    percents = round(100.0 * rownum / float(totalCnt), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    now_time = time.time()
    elapsed_time = int(now_time - start_time)

    sys.stdout.write('[%d/%d] [%s] %s%s, %d sec...%s\r' % (file_cnt, total_file_cnt, bar, percents, '%', elapsed_time, status))
    sys.stdout.flush()






# csv 데이터 check 및 타입확인
def DataTypeFunc(file_path, file_cnt, total_file_cnt, headerList = []):
    rownum = 1

    headerList = headerList
    valueList = []
    lengthList = []


    totalCnt = sum(1 for line in open(file_path))

    with open(file_path, 'r') as f:
        for row in csv.reader(f, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True):
            try:
                if file_cnt == 1 and rownum == 1 :
                    for r in row:
                        r = r.strip().replace(' ','_')
                        headerList.append(r)
                        lengthList.append(['',0,0])
                    rownum += 1

                elif file_cnt > 1 and rownum == 1:
                    for r in row:
                        r = r.strip().replace(' ','_')
                        lengthList.append(['',0,0])
                        valueList.append([regDataType(r), r])
                    rownum += 1

                elif rownum == 2 :
                    for r in row:
                        valueList.append([regDataType(r), r])
                    rownum += 1

                else:
                    for r in range(len(row)):
                        if lengthList[r][1] < len(row[r]):
                            lengthList[r][0] = row[r]
                            lengthList[r][1] = len(row[r])
                            lengthList[r][2] = str(rownum)
                    rownum += 1

                if rownum % 10000 == 0:
                    progress(rownum, total_file_cnt, file_cnt, totalCnt, start_time)


            except Exception as e:
                print('error File & RowNum : ' , file_path, rownum)
                print('error Msg : ', e)
                break

    rowCount = rownum - 1

    file_name_group = file_path.split('//')
    file_name = file_name_group[1]

    DataTypeList = []
    for k in range(len(headerList)):
        DataTypeList.append([headerList[k], valueList[k][0], valueList[k][1], lengthList[k][0], lengthList[k][1], file_name, lengthList[k][2] ])


    return headerList, DataTypeList, rowCount




def printResult(DataTypeList, rowCount, file_size_bytes, file_path, file_cnt):

    headerLine = [['COLUMN_NAME', 'PREDICT_DATA_TYPE', '1ST_ROW_VALUE', 'MAX_LENGTH_VALUE', 'MAX_LENGTH', 'MAX_OCCUR_FILE_NAME', 'MAX_OCCUR_ROWNUM']]
    borderLine = [['-------------', '-------------', '-------------', '-------------', '-------------', '-------------', '-------------']]
    printList = headerLine + borderLine + DataTypeList
    print('\n\n')
    for row in printList:
        line = ''
        for i in range(len(row)):
            if len(str(row[i])) < 22:
                line += str(row[i]) + ' ' * (24 - len(str(row[i])))
            else:
                line += str(row[i])[:20] + '..  '
        print(line)

    end_time = time.time()

    elapsedTime = end_time - start_time
    file_size_conv = str(convert_bytes(file_size_bytes))

    if file_cnt > 1 :
        file_path = '(Dir)' + file_path

    print('--' * 20)
    print('File location : %s \nFile Count : %d' % (file_path, file_cnt))
    print('File size : %s \nTotal Row(s) : %d \nTotal Elapsed Time : %f sec' % (file_size_conv, rowCount, elapsedTime))




def listMaxExchange(listA, listB, target_col=5):
    # 0컬럼 반영
    target_col = target_col - 1

    for i in range(len(listA)):
        if listA[i][target_col] < listB[i][target_col]:
            listA[i] = listB[i]
    return listA





if __name__=="__main__":

    try:
        # file_path = '100 Sales Records.csv'
        # file_path = '1500000 Sales Records.csv'
        # file_path = 'tar_test_short2'

        file_path = sys.argv[1]


        start_time = time.time()
        total = 0
        file_size_bytes = 0
        file_cnt = 0

        # folder case
        if os.path.isdir(file_path):
            file_list = os.listdir(file_path)
            totalDataTypeList = []
            total_file_cnt = len(file_list)
            # multi file : 1st header include but else 0
            totalRowCount = total_file_cnt - 1

            for file in file_list:
                each_file = file_path + '//' + file
                file_size_bytes += os.path.getsize(each_file)
                file_cnt += 1

                if len(totalDataTypeList) == 0:
                    headerList, DataTypeList, rowCount = DataTypeFunc(each_file, file_cnt, total_file_cnt)
                    totalDataTypeList = DataTypeList
                else:
                    headerList, DataTypeList, rowCount = DataTypeFunc(each_file, file_cnt, total_file_cnt, headerList)
                    totalDataTypeList = listMaxExchange(totalDataTypeList, DataTypeList)
                totalRowCount += rowCount

            printResult(totalDataTypeList, totalRowCount, file_size_bytes, file_path, file_cnt)


        # file case
        else:
            file_size_bytes += os.path.getsize(file_path)
            file_cnt = 1
            total_file_cnt = 1

            headerList, DataTypeList, rowCount = DataTypeFunc(file_path, file_cnt, total_file_cnt)
            printResult(DataTypeList, rowCount, file_size_bytes, file_path, file_cnt)

    except:
        print('''Missing CSV file/folder Name. Please retry \n <file usage> \n> python3 CSV2TableCreator.py Sales_Records.csv 
            \n <Dir usage> \n> python3 CSV2TableCreator.py csv_directory ''')