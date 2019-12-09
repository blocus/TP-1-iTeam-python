n = int(input("Entrer le maximum de la suite : "))
def fib(n):
    u = [1, 1]
    for i in range(2,n) :
        u.append(u[i-1] + u[i-2])
    return u[-1]

print(fib(n))
