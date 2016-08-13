# -*- coding=utf-8 -*-
import tushare as ts
import matplotlib.pyplot as plt
import time
# to analyse movie data


plt.axis([0, 48, 0, 6000])
plt.ion()
plt.grid(True)

index = 1
pre_movie_box1 = 0
pre_movie_box2 = 0
pre_movie_box3 = 0
pre_movie_box4 = 0
pre_movie_box5 = 0
while True:
    movie_df = ts.realtime_boxoffice()
    print(movie_df)
    # t = datetime.datetime.now()
    t = time.localtime()
    shituxingzhe_df = movie_df[movie_df['MovieName'] == u'使徒行者']
    weiweiyixiao_df = movie_df[movie_df['MovieName'] == u'微微一笑很倾城']
    daomubiji_df = movie_df[movie_df['MovieName'] == u'盗墓笔记']
    weicheng_df = movie_df[movie_df['MovieName'] == u'危城']
    aichongdajimi_df = movie_df[movie_df['MovieName'] == u'爱宠大机密']
    print index
    print(str(float(shituxingzhe_df.iloc[0, 0]))+','+str(float(weiweiyixiao_df.iloc[0, 0]))+',' +
          str(float(daomubiji_df.iloc[0, 0]))+','+str(float(weicheng_df.iloc[0, 0]))+',' +
          str(float(aichongdajimi_df.iloc[0, 0])))
    plt.plot([index-1, index], [pre_movie_box1, float(shituxingzhe_df.iloc[0, 0])], c='b')
    plt.plot([index-1, index], [pre_movie_box2, float(weiweiyixiao_df.iloc[0, 0])], c='r')
    plt.plot([index-1, index], [pre_movie_box3, float(daomubiji_df.iloc[0, 0])], c='g')
    plt.plot([index-1, index], [pre_movie_box4, float(weicheng_df.iloc[0, 0])], c='k')
    plt.plot([index-1, index], [pre_movie_box5, float(aichongdajimi_df.iloc[0, 0])], c='c')
    pre_movie_box1 = float(shituxingzhe_df.iloc[0, 0])
    pre_movie_box2 = float(weiweiyixiao_df.iloc[0, 0])
    pre_movie_box3 = float(daomubiji_df.iloc[0, 0])
    pre_movie_box4 = float(weicheng_df.iloc[0, 0])
    pre_movie_box5 = float(aichongdajimi_df.iloc[0, 0])
    index += 1
    # print movie_df
    plt.pause(1800)   # update per minute
