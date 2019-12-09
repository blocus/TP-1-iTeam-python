# coding utf-8

minInterval = int(input("Donner la borne inférieure :"))
maxInterval = int(input("Donner la borne supérieure  :"))
n = int(input("Donner un nombre :"))


if n >= minInterval and n <= maxInterval:
    print(n , 'appartient à [',minInterval,',',maxInterval,']')
else:
    print(n , 'n\'appartient pas à [',minInterval,',',maxInterval,']')
