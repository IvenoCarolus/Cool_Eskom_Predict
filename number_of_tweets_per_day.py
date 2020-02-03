def number_of_tweets_per_day(df):
  dates_list = date_parser([date for date in df['Date']])
  date_dic = {}
  for date in dates_list:
    date_dic[date] = dates_list.count(date)
  return (pd.DataFrame(date_dic.values(),date_dic.keys()))[::-1]
