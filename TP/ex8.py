import random
r = random.randint(0, 1000)

d = 100
tentative = 0

while True:
    n = int(input("Donner un nombre : "))
    if(n == r):
        break
    tentative += 1
    tmp = abs(n - r)
    if tmp < d :
        d = tmp
        print("Vous raprochez")
    else:
        print("Vous éloignez")

print("Bravo vous avez trouvé le trésor après", tentative, "fois")
