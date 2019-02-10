import time

# # test_numpy_csv.py
# from numpy import genfromtxt
# start_time = time.time()
# train = genfromtxt('1500000 Sales Records.csv', delimiter=',')
# print(time.time() - start_time) # 23.800432205200195


# test_pandas.py
# from pandas import read_csv
import pandas as pd
start_time = time.time()
# df = pd.read_csv('1500000 Sales Records.csv', sep=",", dtype="unicode")
df = pd.read_csv('1500000 Sales Records.csv')
print(time.time() - start_time) # 2.9763076305389404
print(df.shape)
print(df.columns)
print(df.head())
print(df.tail())
# https://nittaku.tistory.com/114