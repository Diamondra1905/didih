def traiter_choix():
    print("\n===Que souhaitez-vous boire?===")
    print("1- Café☕")
    print("2- Thé🍵")
    print("3- Eau chaude🥛")
    print("4- Quitter Menu")

def gerer_choix():
    commandes = []
    while True:
        traiter_choix()
        # try:
        choix = int(input("Faites votre choix :")); 
        # except ValueError: #(gerer erreur)
        #     print("❌ Veuillez entrer un nombre.")
        #     continue
        if choix == 1:
            print("Vous avez choisi un café ☕")
            commandes.append("Café")
        elif choix == 2:
            print("Vous avez choisi le thé 🍵")
            commandes.append("Thé")
        elif choix == 3:
            print("Vous avez choisi l'eau chaude 🥛")
            commandes.append("Eau chaude")
        elif choix == 4:
            print("Vous avez quitté le menu")
            break
        else:
            print("❌ Votre choix n'est pas répertorié")

    print("\n🧾 Votre commande :")
    if commandes:
        compteur = {}
        pluriel = {"Café": "Cafés", "Thé": "Thés", "Eau chaude": "Eaux chaudes"}
        for boisson in commandes:
            compteur[boisson] = compteur.get(boisson, 0) + 1
        for boisson, nombre in compteur.items():#mamoka kye sy value
            nom_boisson = boisson if nombre == 1 else pluriel.get(boisson, boisson + "s")
            print(f"{nombre} {nom_boisson}")
    else:
        print("Aucune boisson n'a été commandée.")