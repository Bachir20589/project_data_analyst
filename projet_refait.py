import csv
s=0
age_total=0
nombre_etudiant=0
age_moyenne=0
with open("etudiant.csv","r") as f:
    l=csv.DictReader(f)
    for li in l:
        print(li["nom"] + " a " + (li["age"]) + " ans et est en " + li["filiere"])
        if (li["filiere"]=="ING1"):
            s=s+1
        age_total=age_total+int(li["age"])
        nombre_etudiant=nombre_etudiant+1
    age_moyenne=age_total/nombre_etudiant
    print(s)
    print(age_moyenne)
    
    