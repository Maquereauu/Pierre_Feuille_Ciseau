from random import randint
def pierre_feuille_ciseaux(multiplayer:bool,first_game=1):

    pts_p1 = 0
    pts_p2 = 0
    dict_pcs={"pierre":["Bat les ciseaux",0,"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""],
"feuille":["Bat la pierre",1,"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""],
"ciseaux":["Bat la feuille",2,"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]}
    if first_game:
        rules=int(input("Souhaitez vous connaître les règles?(0=>Non)"))
        if rules:
            for k in dict_pcs:
                print(k,dict_pcs[k][0:2])
    if multiplayer:
        while pts_p1 < 3 and pts_p2 < 3:
            p1=input("p1 : Quel coup voulez vous faire?")
            if p1 in dict_pcs:
                print(dict_pcs[p1][2])
                p1 = dict_pcs[p1][1]
            else:
                try:
                    int(p1)
                except ValueError:
                    print("Ce n'est pas un coup possible >:(")
                    continue
                p1 = int(p1)
                if p1 > 2:
                    print("Ce n'est pas un coup possible >:(")
                for keys in dict_pcs.keys():
                    if p1 == dict_pcs[keys][1]:
                        print(dict_pcs[keys][2])
            p2=input("p2 : Quel coup voulez vous faire?")
            if p2 in dict_pcs:
                print(dict_pcs[p2][2])
                p2 = dict_pcs[p2][1]
            else:
                try:
                    int(p2)
                except ValueError:
                    print("Ce n'est pas un coup possible >:(")
                    continue
                p2 = int(p2)
                if p2 > 2:
                    print("Ce n'est pas un coup possible >:(")
                for keys in dict_pcs.keys():
                    if p2 == dict_pcs[keys][1]:
                        print(dict_pcs[keys][2])
            if p1 == p2:
                print("Draw")
            if p1 == 0 and p2 == 1:
                pts_p2 += 1
                print("p2 gagne ce round")
            if p1 == 0 and p2 == 2:
                pts_p1 += 1
                print("p1 gagne ce round")
            if p1 == 1 and p2 == 0:
                pts_p1 += 1
                print("p1 gagne ce round")
            if p1 == 2 and p2 == 0:
                pts_p2 += 1
                print("p2 gagne ce round")
            if p1 == 2 and p2 == 1:
                pts_p1 += 1
                print("p1 gagne ce round")
            if p1 == 1 and p2 == 2:
                pts_p2 += 1
                print("p2 gagne ce round")
        if pts_p1 > pts_p2:
            print("Le gagnant est p1")
        else:
            print("Le gagnant est p2")
        replay=str(input("voulez vous rejouer? oui/non "))
        if replay=="oui":
            return pierre_feuille_ciseaux(1,0)
    if multiplayer == 0:
        while pts_p1 < 3 and pts_p2 < 3:
            p1=input("p1 : Quel coup voulez vous faire?")
            if p1 in dict_pcs:
                print(dict_pcs[p1][2])
                p1 = dict_pcs[p1][1]
            else:
                try:
                    int(p1)
                except ValueError:
                    print("Ce n'est pas un coup possible >:(")
                    continue
                p1 = int(p1)
                if p1 > 2:
                    print("Ce n'est pas un coup possible >:(")
                for keys in dict_pcs.keys():
                    if p1 == dict_pcs[keys][1]:
                        print(dict_pcs[keys][2])
            p2 = randint(0,2)
            for keys in dict_pcs.keys():
                    if p1 == dict_pcs[keys][1]:
                        print(dict_pcs[keys][2])
            if p1 == p2:
                print("Draw")
            if p1 == 0 and p2 == 1:
                pts_p2 += 1
                print("p2 gagne ce round")
            if p1 == 0 and p2 == 2:
                pts_p1 += 1
                print("p1 gagne ce round")
            if p1 == 1 and p2 == 0:
                pts_p1 += 1
                print("p1 gagne ce round")
            if p1 == 2 and p2 == 0:
                pts_p2 += 1
                print("p2 gagne ce round")
            if p1 == 2 and p2 == 1:
                pts_p1 += 1
                print("p1 gagne ce round")
            if p1 == 1 and p2 == 2:
                pts_p2 += 1
                print("p2 gagne ce round")
        if pts_p1 > pts_p2:
            print("Le gagnant est p1")
        else:
            print("Le gagnant est p2")
        replay=str(input("voulez vous rejouer? oui/non "))
        if replay=="oui":
            return pierre_feuille_ciseaux(0,0)
    return "GG"
print(pierre_feuille_ciseaux(0))
