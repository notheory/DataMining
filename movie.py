import tushare as ts
# to analyse movie data

movie_df = ts.realtime_boxoffice()
print movie_df
