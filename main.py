nombres= []
historique=[]


def calculatrice(nombres):

    # permet a l'utilsateur de choisir qu'elle operation veut il faire ?
        print ("Quelle opération voulez-vous effectuer?")

        print("1 addition")
        print("2 soustraction")
        print("3 multiplication")
        print("4 division")

        choix = input() #permet de recueillir l'entrée de l'utilisateur et de la stocker dans la variable choix. Cette valeur représente la sélection de l'opération que l'utilisateur souhaite effectuer.


# operation addition
        if choix=="addition": #si le choix de l'utilisateur est addition
            while True : # permet de crée une boucle infinie qui continue jusqu'a l'instruction de sortie soit rencontré
                nombre= input("entrez un nombre (ou tapez '=' pour terminer:)") # permet a l'utilisateur d'entrer le nombre qu'il souhaite

                if nombre == '=': #des que l'utilsateur tape '=' la boucle se termine
                    break

                try:
                    nombres.append(float(nombre)) #permet d'ajouter les nombres saisis par l'utilsateur dans une liste
                except ValueError:
                    print("Erreur : Veuillez entrer un nombre valide.")
                    continue 
            

            if len(nombres) >=2: #si la longueur de la liste prend minimum 2 nombres

                resultat= sum(nombres)

                print("le resultat de l'addition est:", resultat)
        
    # operation soustraction
        elif choix=="soustraction":
            while True :
                nombre= input("entrez un nombre (ou tapez '=' pour terminer:)")

                if nombre == '=':
                    break

                try:
                    nombres.append(float(nombre))
                except ValueError:
                    print("Erreur : Veuillez entrer un nombre valide.")
                    continue

            if len(nombres) >=2:
                resultat = nombres[0]

            
            for nombre in nombres[1:]:
                resultat -= nombre

            print("le resultat de la soustraction est :", resultat)

    # operation multiplication
        elif choix == "multiplication":
            while True:
                nombre= input("entrez un nombre(ou tapez '=' pour terminer:)")

                if nombre == '=':
                    break

                try:
                    nombres.append(float(nombre))
                except ValueError:
                    print("Erreur : Veuillez entrer un nombre valide.")
                    continue

            if len(nombres) >=2:
                resultat = nombres [0]

            for nombre in nombres[1:]:
                resultat *= nombre

            print ("le resultat de la multiplication:", resultat)

    # operation division
        elif choix == "division":
            while True:
                nombre = input("entrez un nombre(ou tapez '=' pour terminer:)")

                if nombre == '=':
                    break

                try:
                    nombres.append(float(nombre))
                except ValueError:
                    print("Erreur : Veuillez entrer un nombre valide.")
                    continue


            if len(nombres):
                resultat = nombres [0]

            for nombre in nombres[1:]:
                if nombre != 0:  # Éviter la division par zéro
                    resultat /= nombre
                else:
                    print("Erreur : Division par zéro.")
                    resultat = None
                    break

                
            print("le resultat de la division est:", resultat)
        
                
        




calculatrice(nombres)




            

            
            

        

# def expression_math(nombres):
#     print ("Quelle opération voulez-vous effectuer?")

#     print("1 addition")
#     print("2 soustraction")
#     print("3 multiplication")
#     print("4 division")

#     choix = input()

#     if choix == "addition, soustraction":
#         while True:

        



