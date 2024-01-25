# Password generator

## Vue d'ensemble

Implémentation d'un simple générateur de mot de passe.  
Les mots de passe générés contiennent certaines conditions:

- Une longueur supérieure ou égale à 15
- Impossibilité d'avoir une lettre identique ou successive par rapport au dernier caractère (cette condition ne s'appliquera pas pour les nombres)
- Le mot de passe sera séparé en 3 ou 4 parties par des '-'

## Comment générer un mot de passe

1. Exécutez simplement:

```bash
python main.py
```
Cela génèrera un mot de passe de 30 caractères, modifiez le paramètre donné à la méthode dans le fichier `main.py` pour une longueur différente.

## Résistance

Vous pouvez tester la robustesse du mot de passe via ce site: https://www.security.org/how-secure-is-my-password/  
Il en existe plusieurs et donc vérifier également sur différents sites.

## Version / Langage

- Current version: v2023-2024
- Langage: Python
