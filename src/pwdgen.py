from random import randint

ascii = {
            "nombres": [0,1,2,3,4,5,6,7,8,9], 
            "lettres": ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        }

def generateur(longueur):
    
    # longueur est un entier et supérieure à 15 (condition: doit être divisible par 3 ou 4)
    if not isinstance(longueur, int) or longueur < 15 or longueur % 3 != 0 and longueur % 4 != 0:
        print("La longueur doit être un entier supérieur à 15, divisible par 3 ou 4.")
        return None
    
    # mdp sera divisé en 3 ou 4 parties selon la longueur
    if longueur % 3 == 0:
        partie = 3
    else:
        partie = 4
    
    
    password = ""
    # génère les parties du mot de passe
    for i in range (0, partie):
        index_maj = randint(i*(longueur//partie), (i+1)*(longueur//partie)-1) # endroit où on mettra une majuscule
        for j in range (i*(longueur//partie), (i+1)*(longueur//partie)):
            if j == index_maj: # si l'index j est égal à l'index où on mettra une majuscule
                maj = ascii["lettres"][randint(0, len(ascii["lettres"])-1)].upper()
                if i != 0 and j != 0:
                    while (maj in [chr(ord(password[-1]) + 1), chr(ord(password[-1]) - 1), password[-1]]):
                        maj = ascii["lettres"][randint(0, len(ascii["lettres"])-1)].upper()
                password += maj
            else:
                type_car = randint(0,1) # 0 = nombre, 1 = lettre
                if type_car == 0:
                    number = str(ascii["nombres"][randint(0, len(ascii["nombres"])-1)])
                    password += number
                else:
                    minu = ascii["lettres"][randint(0, len(ascii["lettres"])-1)]
                    if i != 0 and j != 0:
                        # on vérifie que la lettre n'est pas la même que la précédente ou qu'elle n'est pas la lettre précédente +1 ou -1 dans l'alphabet
                        while (minu in [chr(ord(password[-1]) + 1), chr(ord(password[-1]) - 1), password[-1]]):
                            minu = ascii["lettres"][randint(0, len(ascii["lettres"])-1)]
                    password += minu
        if i != partie-1: # si on est pas à la dernière partie
            password += "-"
    
    return password