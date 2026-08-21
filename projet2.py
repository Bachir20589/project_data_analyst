import csv

with open("etudiant.csv", "rt") as f:
    lecteur = csv.DictReader(f)
    
    nb_ing1 = 0
    somme_age = 0
    nb_etudiants = 4
    
    for ligne in lecteur:
        # 1. Affichage de chaque étudiant
        print(ligne["nom"] + " a " + ligne["age"] + " ans et est en " + ligne["filiere"])
        
        # 2. Comptage des étudiants en ING1
        if ligne["filiere"] == "ING1":
            nb_ing1 = nb_ing1 + 1
        
        # 3. Accumulation pour la moyenne
        somme_age = somme_age + int(ligne["age"])
        # nb_etudiants = nb_etudiants + 1
    
    # 4. Résultats finaux (après la boucle)
    print("Nombre d'étudiants en ING1 :", nb_ing1)
    moyenne = somme_age / nb_etudiants
    print("Âge moyen :", moyenne)