import pwdgen

def main(taille):
    print("Génération d'un mot de passe...")
    pwd = pwdgen.generateur(taille)
    if pwd is not None:
        print(pwd)
    
if __name__ == "__main__":
    main(30)