# TP-1-iTeam-python

## Exercices faciles

### Exercice 1

Ecrire un programme qui permet :

1. Saisir deux entiers et affiche leur somme et leur produit.
2. Echange les deux entiers saisis et les affiches avant et après l'échange.

Modifier ensuite le programme afin de saisir deux réels.

## les structures conditionnelles

### Exercice 2

Ecrire un programme qui permet de déterminer si un entier saisi est divisible par 2, 3, 5, 7, 11 et 13.

### Exercice 3
Ecrire un programme qui permet de déterminer la mention d'une moyenne saisie:
- 0 < moyenne <10 : Redoublant.
- 10 <= moyenne < 12  : Passable.
- 12 <= moyenne < 14  : Assez bien.
- 14 <= moyenne < 16  : Bien.
- 16 <= moyenne < 18  : Très bien.
- 18 <= moyenne <= 20  : Excellent.
- Sinon il affiche une erreur.


### Exercice 4
Ecrire un programme qui permet de saisir un nombre puis détermine s’il appartient à un intervalle donné, sachant que les extrémités de l’intervalle sont fixées par l’utilisateur.

## les structures itératives
### Exercice 5
Ecrire un programme qui décompose un nombre saisi en facteur de nombres premiers et les affiche.

### Exercice 6
- Initialisez deux entiers : `a = 0` et `b = 10`.
- Écrire une boucle affichant et incrémentant la valeur de `a` tant qu’elle reste inférieure
à celle de `b`.
- Écrire une autre boucle décrémentant la valeur de `b` et affichant sa valeur si elle est impaire. Boucler tant que `b` n’est pas nul.

### Exercice 7
Ecrire un programme qui affiche tous les nombres premiers entre 2 et un nombre `n` saisi.

### Exercice 8
Ecrire un programme qui :
- génére un nombre `r` aléatoire entre 0 et 1000.
- Initialisez un entier `d = 100` qui va servir à la distance.
- Le programme va demander un nombre `n` de l'utilisateur.
    - Si `|r - n| < d`, le programme affiche que l'utilisateur se raproche et mis à jour `d`
    - Sinon le programme affiche que l'utilisateur s'éloigne.

Le programme s'arrète lorsque l'utilisateur saisi le nombre `r` et affiche combien de tentatives effectué par l'utilisateur.


## Gestion des exceptions

### Exercice 9
Ecrire un programme qui permet de saisir un nombre entier et le convertir sinon elle redemande la saisie de ce nombre.


## les structures fonctionelles

### Exercice 10
Ecrire une fonction qui s'appelle `calc` qui a comme paramètre une chaine de caractères qui comptien une equation et cette fonction permet de la calculer.

### Exercice 11
- Ecrire une fonction qui prend en paramètre un entier `n` et retourne `True` si `n` est premier.
- Modifier l'`Exercice 7` en utilisant cette fonction.

### Exercice 12

Ecrire une fonction qui prend un entier `n` et retourne le Nième élément de la suite de Fibonacci. La suite de Fibonacci est définie comme suivant :

- U_{0} = U_{1} = 1
- U_{n} = U_{n-1} + U_{n-2}
