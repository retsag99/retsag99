from constant import *
from case import *
from boat import *
from random import randint

def création_grille():
    global longeur
    global largeur
    grille=[]
    nb_case_X=longeur//32
    nb_cas_Y=largeur//32
    for case_X in range(nb_case_X):
        sub_grille=[]
        for case_Y in range(nb_cas_Y):
            sub_grille.append(Case(case_X,case_Y))
        grille.append(sub_grille)
    return grille

def initialisation_grille(grille):
    for ligne in grille:
        for case in ligne:
            if randint(0,1):
                case.set_hasboat()
                if randint(0,1):
                    case.set_boat(boat_dict["platforme_touche"])
    return grille

def grille_update(grille,pos_X,pos_Y):
    case=grille[pos_X][pos_Y]
    case.set_esttouche==True
    if case.get_hasboat==True:
        case.set_image("")

if __name__=="__main__":
    grille_test=création_grille()
    grille_test=initialisation_grille(grille_test)
    print(grille_test)
    for ligne in grille_test:
        for case in ligne:
            print(f"{case}",end='')
        print("")