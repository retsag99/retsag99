import pygame

#colors
ROUGE=(255,0,0)
BLEU=(0,0,255)
VERT=(0,255,0)
JAUNE=(255,255,0)
BLANC=(255,255,255)
GRIS_CLAIRE=(192,192,192)
GRIS=(128,128,128)
GRIS_FONCE=(64,64,64)
NOIRE=(0,0,0)

#taille
longeur= 320
largeur= 320
length=0
height=0

#joueur
taille_joueur=10
player_coin=round(taille_joueur/2,0)
Joueur_X=250
Joueur_Y=250

#oiseau
taille_oiseau=10
oiseau_coin=round(taille_oiseau/2,0)
Oiseau_X=0
Oiseau_Y=0
ligne_de_vol=50

#image
eau_non_decouverte=pygame.image.load("images\\eau_non_decouverte.png")
eau_touche_avec_bateau=pygame.image.load("images\eau_touche_avec_bateau.png")
eau_touche_sans_bateau=pygame.image.load("images\eau_touche_sans_bateau.png")
platforme_non_touche=pygame.image.load("images\platforme_non_touche.png")
platforme_touche=pygame.image.load("images\platforme_touche.png")
petit_bateau_bas=pygame.image.load("images\petit_bateau_bas.png")