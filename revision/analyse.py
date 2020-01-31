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

entree = input("Donner Nom à chercher : ")

data = {}
test = False
for d in donnee:
    if d['nom'].upper() == entree.upper():
        test = True
        data = d
        break

if test:
    print(entree, "Trouvé")
    print(data["nom"], data['prenom'])
else:
    print("CIN Introuvable")
