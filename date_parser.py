#!
def date_parser(list_dates):
  just_dates = []
  for d_string in list_dates:
    just_dates.append(d_string[0:10])
  return just_dates
