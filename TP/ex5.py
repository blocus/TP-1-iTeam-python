n = int(input("Donner un nombre :"))

primeList = []

i = 2
while i <= n:
    if(n % i == 0):
        test = True
        for p in primeList:
            if i % p == 0:
                test = False
                break
        if test == True:
            primeList.append(i)
            print(i, "divise", n)
    i += 1
