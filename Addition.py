def addition(*num):
  _num = 0
  for i in num:
    _num+=i
    yield _num
print(addition(2,3,4,5,6,7,7,6,5))
