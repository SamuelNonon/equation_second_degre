from math import sqrt

def sec_deg () :
    print ("Ce programme permet de résoudre des équations de second degré")
    print ("Rentrez d'abord les coéficiants et vous sera renvoyé" \
           "la ou les solutions lesquels l'équation est égale à zéro")
    a = float (input ("Choisir un nombre différent de 0 pour a  "))
    b = float (input ("Choisir un nombre pour b  "))
    c = float (input ("Choisir un nombre pour c  "))
    delta = b **2 - 4 * a * c
    if delta == 0 :
        x0 = -b / 2 * a
        return "La solution de l'équation est ", x0
    elif delta < 0 :
        return "Il n'y a pas de solutions"
    else :
        x1 = (- b - sqrt (delta)) / (2 * a)
        x2 = (- b + sqrt (delta)) / (2 * a)
        return "Les solutions de l'équation sont ", x1, " et ", x2
