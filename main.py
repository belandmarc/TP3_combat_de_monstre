
# Programme fait par Marc-Aurèle Béland
# TP3 - Combat des monstres
# Groupe 406


from random import randint

niveau_vie = 20
force_adversaire = 0
numero_adversaire = 0
numero_combat = 0
nombre_defaites = 0
score_de = 0
combat_statut = 0
nombre_victoires_consecutives = 0
continuer = True
afficher_regle = True

while continuer:

    if afficher_regle:
        afficher_regle = False
    else:
        force_adversaire = randint(1, 6)

    if nombre_victoires_consecutives % 3 == 0 and nombre_victoires_consecutives != 0:
        force_adversaire = randint(4, 5)
        print(f"vous êtes tombé contre un boss")

    print(f'Vous tombez face à face avec un adversaire de difficulté : {force_adversaire} ')
    choix_menu = int(input(f"Que voulez-vous faire?\n1 - Combatre le monstre\n2 - Contourner le monstre"
                           f"\n3 - Afficher les règles du jeu\n4 - Quitter la partie"))

    if choix_menu == 1:
        print(f"vous-decidez de combattre le monstre")
        score_de = randint(1, 6)
        numero_combat += 1

        if score_de > force_adversaire:
            print(f"vous avez battue le montre")
            niveau_vie += force_adversaire
            print(f"vous avez {niveau_vie} vies")
            print(f"vous êtes à votre {numero_combat}ème combat")
            nombre_victoires_consecutives += 1
            print(f"vous êtes à {nombre_victoires_consecutives} victoire consécutives")
        if score_de <= force_adversaire:
            nombre_victoires_consecutives = 0
            print(f"le monstre est plus puissant que vous")
            niveau_vie -= force_adversaire
            print(f"vous avez {niveau_vie} vies")
            print(f"vous êtes à votre {numero_combat}ème combat")
            nombre_defaites += 1
            print(f"vous êtes à {nombre_defaites} défaites")

    elif choix_menu == 2:
        print(f"vous perdez une vie")
        niveau_vie -= 1
        print(f"vous avez {niveau_vie} vies")

    elif choix_menu == 3:

        print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.")
        print(f"Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.")
        print(
            f"Une défaite a lieu lorsque la valeur du dé lancé par "
            f"l’usager est inférieure ou égale à la force de l’adversaire.")
        print(f"Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.")
        afficher_regle = True

    elif choix_menu == 4:
        print(f"Merci et au revoir")
        continuer = False

    if niveau_vie == 0:
        print(f"vous avez perdu")
        continuer = False
