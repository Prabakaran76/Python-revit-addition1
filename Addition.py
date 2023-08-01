def addition(*num):
    _num = 0
    for i in num:
        _num += i
        yield _num
result = addition(1,2,3,4,5,67,78)
for i in result:
    print(i) #result will be printed