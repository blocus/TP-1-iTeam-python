file = open("data.txt", "r") # Ouverture du fichier

donnee = [] # Création de la liste

# Lire le fichier et l'organiser

for line in file:
    line = line[:-1] # Enlever le \n
    line = line.split(';') # diviser la chaine
    d = { # Creation de la structure
        'nom' : line[0],
        'prenom': line[1],
        'cin' : line[2]
    }
    donnee.append(d) # Ajout dans la liste

entree = input("Recherche [key:value] : ")
entree = entree.split(':', 1)

key = None
value = None
if len(entree) == 2:
    key = entree[0]
    value = entree[1]
else:
    value = entree[0]

data = {}
test = False
for d in donnee:
    if key == None:
        for k in d.keys():
            if d[k].upper() == value.upper():
                test = True
                data = d
                break
        if test:
            break
    else:
        if key in d:
            if d[key].upper() == value.upper():
                test = True
                data = d
                break

if test:
    print(entree, "Trouvé")
    print(data["nom"], data['prenom'])
else:
    print(" Introuvable")
