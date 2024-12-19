"""
Ce script encode une chaîne de caractères en une liste de tuples contenant les caractères 
et leur nombre d'occurrences consécutives. Deux approches sont utilisées :
une itérative et une récursive.
"""
#### Imports et définition des variables globales
import sys
sys.setrecursionlimit(1500) ### fonction trouvé sur le site
##https://stackoverflow.com/questions/3323001/
##what-is-the-maximum-recursion-depth-and-how-to-increase-it
#### Fonctions secondaires
def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères
     passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    if len(s) == 0:
        return []
    liste_tuple = []
    nouveau_char = s[0]
    occ = 1
    for char in s[1:]:
        if char == nouveau_char:
            occ += 1
        else:
            liste_tuple.append((nouveau_char, occ))
            nouveau_char = char
            occ = 1
    liste_tuple.append((nouveau_char, occ))
    return liste_tuple

def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    # cas de base
    if len(s) == 0:
        return []
    # recherche nombre de caractères identiques au premier
    premier_char = s[0]
    occ = 1
    while occ < len(s) and s[occ] == premier_char:
        occ += 1
    # appel récursif
    return [(premier_char, occ)] + artcode_r(s[occ:])
#### Fonction principale

def main():
    """
    Point d'entrée principal du script. 
    Effectue des tests sur les fonctions artcode_i et artcode_r.
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
