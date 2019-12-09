n = int(input("Donner un nombre :"))

listeDiviseurs = [2, 3, 5, 7, 11, 13]
for p in listeDiviseurs:
    if n % p == 0:
        print('Le nombre', n , 'est divisible par', p)
    else:
        print('Le nombre', n , "n'est divisible par", p)
