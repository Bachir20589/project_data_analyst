def add(a,b):
    s=a+b
    return(s)
def sous(a,b):
    d=a-b
    return(d)
def produit(a,b):
    m=a*b
    return(m)
def divison(a,b):
    if (b==0):
        print("b doit etre different de 0")
    else:
        div=a/b
        return(div)
    

a=int(input("donner un entier\n"))

b=int(input("donner un entier\n"))

operation=input("choisi l'operation\n")

def calculatrice(a,b,operation):
    if (operation=="addition"):
        som=add(a,b)
        print(som)
    elif (operation=="soustraction"):
        diff=sous(a,b)
        print(diff)
    elif (operation=="division"):
        divise=divison(a,b)
        print(divise)
    elif (operation=="produit"):
        pro=produit(a,b)
        print(pro)
    else:
        print("y a erreur")
calculatrice(a,b,operation)
while True:
    continuer = input("Autre calcul ? (oui/non)\n")
    if continuer != "oui":
        break
    a = int(input("donner un entier\n"))
    b = int(input("donner un entier\n"))
    operation = input("choisi l'operation\n")

    if operation not in ["addition", "soustraction", "produit", "division"]:
        print("choisi une operation correcte")
    else:
        calculatrice(a, b, operation)



