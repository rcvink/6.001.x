def genPrimes():
    x = 2
    while True:
        isPrime = True
        for i in range(2, x):
            if not x % i:
                isPrime = False
                break
        if isPrime:
            yield x
        x += 1

foo = genPrimes()

for j in range(10000000):
    print(foo.__next__())