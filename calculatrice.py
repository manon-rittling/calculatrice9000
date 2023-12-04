historique = []

# fonction pour que l'utilisateur choisissent qu'elle operation il souhaite executer
def demander_operation():
    print("Quelle opération voulez-vous effectuer?")
    print("1 addition")
    print("2 soustraction")
    print("3 multiplication")
    print("4 division")
    return input()


# fonction pour que l'utilisateur rentre les nombres (entier ou decimaux)  qu'il souhaite pour une operation
def saisir_nombres():
    nombres= [] #liste vide pour mettre les nombres saisi par l'utilisateur
    while True:
        nombre = input("entrez un nombre appuyer sur 'entrer'pour rentrer autre valeur (puis tapez '=' pour terminer):") #permet a l'utilisateur de rentrer un nombre tant qu'il le souhaite
        if nombre == '=': #permet de mettre fin a l'ajout des nombres en tapant sur '= pour avoir le resultat 
            break
        try:
            nombres.append(float(nombre)) # ajoute les nombres a la liste 
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide.") #si l'utilisateur tape une valeur non valide comme un lettre ou erreur de syntaxe ca affichera ce texte

    return nombres

# fonction operation addition
def addition(nombres):
    return sum(nombres)

#fonction operation soustraction
def soustraction(nombres):
    resultat = nombres[0]
    for nombre in nombres [1:]:
        resultat -= nombre
    return resultat

# fonction operation multiplication
def multiplication(nombres):
    resultat = nombres[0]
    for nombre in nombres[1:]:
        resultat *= nombre
    return resultat

# fonction operation division
def division(nombres):
    resultat = nombres[0]
    for nombre in nombres[1:]:
        if nombre !=0:
            resultat /= nombre
        else:
            print("Erreur: division impossible par 0" )
            resultat = None
        
    return resultat

# fonction pour afficher le resulat  
def afficher_resultat(operation, resultat):
    if resultat is not None:
        print(f"le resultat de {operation} est: {resultat}")

#fonction pour ajouter une opeartion a l'historique 
def ajouter_a_historique(operation, nombres, resultat):
    historique.append({
        'operation': operation,
        'nombres': nombres,
        'resultat': resultat
    })

    
# Fonction pour afficher ou effacer l'historique
def afficher_historique():
    choix_historique = input("voulez vous afficher ou effacer l'historique ('o' pour voir et 'n' pour effacer): (o/n)")

    if choix_historique == "o": # si l'utilisateur tape 'o' ca affiche l'historique
        
        for calcul in historique: # Pour chaque calcul dans l'historique, récupère les détails et affiche-les.
            operation = calcul['operation'] # Récupère le type d'opération 
            nombres = calcul['nombres'] # Récupère les nombres utilisés pour l'opération.
            resultat = calcul['resultat'] # Récupère le résultat de l'opération
            print(f"Opération : {operation}, Nombres : {nombres}, Résultat : {resultat}")
    
    elif choix_historique == "n": # Si l'utilisateur choisit de supprimer l'historique.
            historique.clear() # Efface complètement l'historique.
            print("effacé historique")


    # boucle principal et infinie, le programme continuera à s'exécuter tant que cette condition est vraie.
while True:
    choix = demander_operation() # Appelle la fonction pour demander à l'utilisateur quelle opération effectuer et stocke le choix dans la variable 'choix'.

    if choix == "1": #choix correspond a l'addition et l'utilisateur devra taper 1 pour acceder a cette operation
        nombres = saisir_nombres() # Appelle la fonction pour que l'utilisateur entre les nombres pour l'addition.
        if len(nombres) >= 2: # il faut minimum 2 nombres pour pouvoir faire une operation
            resultat = addition(nombres) # Appelle la fonction pour effectuer l'addition
            afficher_resultat("l'addition", resultat) # Affiche le résultat
            ajouter_a_historique("addition", nombres, resultat) # Ajoute l'opération à l'historique.
        else:
            print("Erreur : Vous devez entrer au moins deux nombres pour effectuer une opération.")
        
            

    elif choix == "2":
        nombres = saisir_nombres()
        if len(nombres) >=2:
            resultat = soustraction(nombres)
            afficher_resultat("la soustraction", resultat)
            ajouter_a_historique("soustraction", nombres, resultat)
        else:
            print("Erreur : Vous devez entrer au moins deux nombres pour effectuer une opération.")
        
    elif choix == "3":
        nombres = saisir_nombres()
        if len(nombres) >=2:
            resultat = multiplication(nombres)
            afficher_resultat("la multiplication", resultat)
            ajouter_a_historique("multiplication", nombres, resultat)
        else:
            print("Erreur : Vous devez entrer au moins deux nombres pour effectuer une opération.")

    elif choix == "4":
        nombres = saisir_nombres()
        if len(nombres) >= 2:
            resultat = division(nombres)
            afficher_resultat("la division", resultat)
            ajouter_a_historique("division", nombres, resultat)
        else:
            print("Erreur : Vous devez entrer au moins deux nombres pour effectuer une opération.")


    afficher_historique()

    reponse = input("voulez- vous effectuer une autre opération? (o/n):")
    if reponse.lower() != 'o':
        break # sort de la boucle si la reponse est 'n'









