while True:
    test = True
    try:
        n = int(input("Donner un nombre :"))
    except KeyboardInterrupt:
        break
    except:
        test = False
    if test:
        break
