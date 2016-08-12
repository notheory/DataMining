# -*- coding:utf-8 -*-
import tushare as ts
import time
import matplotlib.pyplot as plt
import numpy as np
import threading
# to analyse stock data

plt.figure(1)
plt.figure(2)
plt.figure(1)
plt.axis([0, 900, 32000000, 60000000])
plt.ion()
plt.title('002024')
plt.xlabel('Time')
plt.ylabel('Volume')
plt.figure(2)
plt.axis([0, 900, 10.06, 12.30])
plt.ion()
plt.title('002024')
plt.xlabel('Time')
plt.ylabel('Price')

i = 0
temp_price = 0
while True:
    df = ts.get_realtime_quotes('002024')
    print(df.at[0, 'volume'])
    plt.figure(1)
    plt.scatter(i, df.loc[0, ['volume']], s=1)
    print(df.at[0, 'price'])
    if df.at[0, 'price'] > temp_price:
        color = 'red'
    elif df.at[0, 'price'] < temp_price:
        color = 'green'
    else:
        color = 'black'
    temp_price = df.at[0, 'price']
    plt.figure(2)
    plt.scatter(i, df.loc[0, ['price']], s=1, c=color)
    i += 1
    plt.pause(5)
