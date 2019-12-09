def fib(n):
    i = 2
    a, b = 1, 1
    while i < n:
        a, b = b, a+b
        i += 1
    print(b)
fib(int(input("Donner un nombre :")))
