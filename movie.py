# -*- coding=utf-8 -*-
import tushare as ts
import matplotlib.pyplot as plt
# to analyse movie data

while True:
    movie_df = ts.realtime_boxoffice()
    shituxingzhe_df = movie_df[movie_df['MovieName']==u'使徒行者']
    weiweiyixiao_df = movie_df[movie_df['MovieName']==u'微微一笑很倾城']
    daomubiji_df = movie_df[movie_df['MovieName']==u'盗墓笔记']
    plt.plot(shituxingzhe_df.at[0, 'BoxOffice'])
    print movie_df
