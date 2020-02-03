def word_splitter(df):
  words_of_words = []
  for tweet in df['Tweets']:
    words_of_words.append(tweet.split(' '))
  return pd.DataFrame({'Tweets': list(df['Tweets']),'Date': list(df['Date']),'Split Tweets': words_of_words})
