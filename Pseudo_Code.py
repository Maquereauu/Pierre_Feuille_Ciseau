#DEBUT
#Importer module random
#définir foncion pierre_feuille_ciseaux avec comme paramètre multiplayer(bool)
    #assigner p1_pts est égal à 0
    #assigner p2_pts est égal à 0
    #assigner dict_pcs avec comme clés les noms des différents coups et en valeur leurs description (quel coup bat lequel ainsi que leurs ids) 
    #assigner à rules le retour de la fonction input demandant si l'utilisateur veut connaître les rêgles est vrai
    #si le retour de la fonction input demandant si l'utilisateur veut connaître les rêgles est vrai
        #alors retourne le dictionnaire
    #si multiplayer vaut 1
        #alors tant que p1_pts < 3 et p2_pts < 3
            #alors assigner p1 est égal à la valeur du retour de la fonction input demandant quel coup veut-il faire
            #si p1 est un str()
                #alors prendre la valeur int de la clé du dictionnaire correspondante au str
            #assigner p2 est égal à la valeur du retour de la fonction input demandant quel coup veut-il faire
            #si p2 est un str()
                #alors prendre la valeur int de la clé du dictionnaire correspondante au str
            #si p1 == p2
                #alors affiche "Draw"
            #si p1 == 0 et p2 == 1
                #alors on incrémente p2_pts de 1
            #si p1 == 0 et p2 == 2
                #alors on incrémente p1_pts de 1
            #si p1 == 1 et p2 == 0
                #alors on incrémente p1_pts de 1
            #si p1 == 2 et p2 == 0
                #alors on incrémente p2_pts de 1
            #si p1 == 2 et p2 == 1
                #alors on incrémente p1_pts de 1
            #si p1 == 1 et p2 == 2
                #alors on incrémente p2_pts de 1
        #si p1_pts > p2_pts 
            #alors afficher str le gagnant est p1
        #sinon
            #alors afficher str le gagnant est p2
        # assigner replay est égal au le retour de la fonction input demandant à l'utilisateur si oui/non il veut rejouer
        #si replay est égal à oui 
            #alors retourner pierre_feuille_ciseaux(1)
    #si multiplayer vaut 0 
        #alors tant que pts_p1 < 3 et pts_p2 < 3
            #alors assigner p1 est égal à la valeur du retour de la fonction input demandant quel coup veut-il faire
            #si p1 est un str()
                #alors prendre la valeur int de la clé du dictionnaire correspondante au str
            #assigner p2 est égal au retour de la fonction randint(0,2)
            #si p1 == p2
                #alors affiche "Draw"
            #si p1 == 0 et p2 == 1
                #alors on incrémente p2_pts de 1
            #si p1 == 0 et p2 == 2
                #alors on incrémente p1_pts de 1
            #si p1 == 1 et p2 == 0
                #alors on incrémente p1_pts de 1
            #si p1 == 2 et p2 == 0
                #alors on incrémente p2_pts de 1
            #si p1 == 2 et p2 == 1
                #alors on incrémente p1_pts de 1
            #si p1 == 1 et p2 == 2
                #alors on incrémente p2_pts de 1
        #si pts_p1 > pts_p2 
            #alors afficher str le gagnant est p1
        #sinon
            #alors afficher str le gagnant est p2
        # assigner replay est égal au retour de la fonction input demandant à l'utilisateur si oui/non il veut rejouer
        #si replay est égal à oui 
            #alors retourner pierre_feuille_ciseaux(0)
#FIN
