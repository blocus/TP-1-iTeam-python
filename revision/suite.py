
def U(Un_1):
    return (Un_1 * 3) -1

seuil = int(input("Donner votre seuil : "))

n = 0
Un = 1
while Un < seuil:
    Un = U(Un)
    n += 1

print("U(",n,') =', Un)
