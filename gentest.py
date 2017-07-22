def genTest():
    i = 0
    while True:
        i += 1
        yield i

foo = genTest()
print(foo.__next__())
print(foo.__next__())
print(foo.__next__())
print(foo.__next__())
print(foo.__next__())
print(foo.__next__())
print(foo.__next__())
print(foo.__next__())
print(foo.__next__())
print(foo.__next__())