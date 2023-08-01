def addition(*num):
  _num = 0
  for i in num:
    _num+=i
    yield _num
result = addition(3,4,5,6,7,8,9,10)
for i in result:
  print(i)
