def five_number_summary(list1):
  #median
  list1.sort()
  if len(list1) % 2 == 0:
    median = (list1[len(list1)//2] + list1[len(list1)//2-1])/2
  else:
    median = list1[len(list1)//2]
  #max
  max_val = max(list1)
  #min
  min_val = min(list1)

  #lower quartile not the correct way
  q1 = round((25/100)*(max_val + min_val),2)
  
  #upper quartile not the correct way
  q3 = round((75/100)*(max_val + min_val),2)

  return ({'Minimum':min_val,'Lower quartile':q1,'Median':median,'Upper quartile':q3,'Maximum':max_val})
