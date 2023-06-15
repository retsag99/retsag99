import sys 
from constant import *
from random import randint
from logique import *

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((longeur,largeur))
eau_non_decouverte.convert()

grille_joueur=création_grille()
grille_joueur=initialisation_grille(grille_joueur)
        
        
game_over=False 

while not game_over :
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type==pygame.MOUSEBUTTONDOWN:
            press=pygame.mouse.get_pressed(3)
            if press[0]:
                co_X,co_Y=int(Joueur_X//32),int(Joueur_Y//32)
                case_chercher=grille_joueur[co_X][co_Y]
                if case_chercher.hasboat==True:
                    if case_chercher.boat_name in boat_dict:
                        case_chercher.set_esttouche()
                        screen.blit(case_chercher.image,((Joueur_X//32)*32,(Joueur_Y//32)*32,taille_joueur,taille_joueur))
                    else:
                        screen.blit(eau_touche_avec_bateau,((Joueur_X//32)*32,(Joueur_Y//32)*32,taille_joueur,taille_joueur))
                else:
                    screen.blit(eau_touche_sans_bateau,((Joueur_X//32)*32,(Joueur_Y//32)*32,taille_joueur,taille_joueur))

    position=pygame.mouse.get_pos()
    Joueur_X,Joueur_Y=position[0]-player_coin,position[1]-player_coin

    lenght=0
    while length<longeur:
        height=0
        while height<largeur:
            screen.blit(eau_non_decouverte,[length,height])
            height=height+32
        length=length+32
    
    #screen.blit(petit_bateau_bas,(Oiseau_X,Oiseau_Y,taille_joueur,taille_joueur))
    #pygame.draw.rect(screen,BLEU,(Joueur_X,Joueur_Y,taille_joueur,taille_joueur))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()