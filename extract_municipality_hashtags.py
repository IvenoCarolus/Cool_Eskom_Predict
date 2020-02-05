def extract_municipality_hashtags(df):
  municipality_dict = { '@CityofCTAlerts' : 'Cape Town',
            '@CityPowerJhb' : 'Johannesburg',
            '@eThekwiniM' : 'eThekwini' ,
            '@EMMInfo' : 'Ekurhuleni',
            '@centlecutility' : 'Mangaung',
            '@NMBmunicipality' : 'Nelson Mandela Bay',
            '@CityTshwane' : 'Tshwane'}
  
  length = len(df['Tweets'])
  mun_list = []
  flag = 0
  for row in df['Tweets']:
    flag = 0
    for key in municipality_dict.keys():
      if key in row:
        mun_list.append(municipality_dict[key])
        flag = 1
        break
    if not flag:
      mun_list.append(np.nan)
  
  final_hash = []
  for row in twitter_df['Tweets']:
    final_hash.append([string for string in row.lower().split() if string[0][0] == '#'])
  final_hash = ['NaN' if x == [] else x for x in final_hash]
  df['hastag'] = final_hash
  df['municipality'] = mun_list
  return df
