def metric_dic(list1):

  #mean
  mean = 0
  for i in list1:
    mean += i
  mean = round(mean / len(list1),2)

  #mode
  mode = 0
  for i in list1:
    if list1.count(i) > mode:
      mode = i
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
  #var
  var = round(sum((i-mean) ** 2 for i in list1)/len(list1),2)

  #std
  std = round(var ** (1/2),2)
  print({'Mean':mean,'Mode':mode,'Median':median,'Maximum':max_val,'Minimum':min_val,'Variance':var,'Standard Deviation':std})
