# -*- coding:utf-8 -*-
import tushare as ts
import time
import matplotlib.pyplot as plt
import numpy as np
import threading
# to analyse stock data
plot_interval = 30      # 数据点间隔
update_interval = 5     # 检测间隔
stock_code = '002024'
while (time.strftime('%H', time.localtime()) != '9' and time.strftime('%M', time.localtime())) != '30' \
        or time.strftime('%H', time.localtime()) != '13':
    pass
open_price = ts.get_realtime_quotes(stock_code).at[0, 'open']   # 开盘价
price_upper = float(open_price) * 1.1       # 计算涨停价格
price_lower = float(open_price) * 0.9       # 计算跌停价格
plt.figure(1)
plt.figure(2)
plt.figure(1)
plt.axis([0, 7200/plot_interval, 0, 35000000])
plt.ion()
plt.title(stock_code)
plt.xlabel('Time')
plt.ylabel('Volume')
plt.figure(2)
plt.axis([0, 7200/plot_interval, price_lower, price_upper])
plt.ion()
plt.title(stock_code)
plt.xlabel('Time')
plt.ylabel('Price')
period = plot_interval/update_interval    # 6个周期内需要重绘
i = 0
plot_i = 0
temp_price = 0.0
while True:
    df = ts.get_realtime_quotes(stock_code)
    print(df.at[0, 'volume'])
    plt.figure(1)
    plt.scatter(i, float(df.at[0, 'volume']), s=1)
    print(df.at[0, 'price'])
    plt.figure(2)
    if df.at[0, 'price'] > open_price:
        color = 'red'
    elif df.at[0, 'price'] < open_price:
        color = 'green'
    else:
        color = 'black'
    if i % period != 0:   # uncertain point
        plt.scatter(plot_i, temp_price, s=1, c='white')     # 抹去上一个点
        plt.scatter(plot_i, float(df.at[0, 'price']), s=1, c=color)  # 绘制新的点
    else:                 # certain point
        plot_i += 1
        plt.scatter(plot_i, float(df.at[0, 'price']), s=1, c=color)
    temp_price = float(df.at[0, 'price'])
    i += 1
    plt.pause(update_interval)
