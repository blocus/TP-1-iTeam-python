n = int(input("Donner un nombre : "))

primeList = []

i = 2
while i <= n:
    test = True
    for p in primeList:
        if i % p == 0:
            test = False
            break
    if test:
        primeList.append(i)
    i += 1
print(primeList)
