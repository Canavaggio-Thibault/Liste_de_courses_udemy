liste = []

Menu = """Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
? Votre choix : """

Choix = ["1", "2", "3", "4", "5"]



while True:
    a = input(Menu)
    if a not in Choix:
        print("Veuillez choisir une option valide !")
        continue
    if a == "1":
        item = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        liste.append(item)
        print(f"L'élément {item} a bien été ajouté à la liste.")
    elif a == "2":
        item = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
        if item in liste:
            liste.remove(item)
        else:
            print(f"L'élément {item} n'est pas dans la liste.")
    elif a == "3": 
       print(liste)
    elif a == "4": 
        liste.clear()
        print("La liste a été vidée de son contenu.")
    elif a == "5":
        break

