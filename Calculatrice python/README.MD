# Configurer votre identité
$ git config --global user.name "Votre Nom"
$ git config --global user.email "email@example.com"

# Vérifier l'installation
$ git --version
$ git config --list

$ git init
Initialiser un nouveau dépôt
$ git status
Voir l'état actuel
$ git add fichier.py
Ajouter un fichier
$ git add .
Ajouter tous les fichiers


$ git commit -m "message"
Créer un commit

$ git log
Voir l'historique

$ git log --oneline
Historique condensé

$ git diff
Voir les modifications


# Créer et initialiser le projet
$ mkdir calculatrice-python
$ cd calculatrice-python
$ git init

# Créer et commiter
$ touch main.py
$ git add main.py
$ git commit -m "feat: structure initiale"
[main abc1234] feat: structure initiale

"""Module principal du projet."""

def
main():
"""Point d'entrée du programme."""
print("Bienvenue!")

if
__name__ == "__main__":
main()

Instructions
1
Créer dossier
exercice-git
et
git init
2
Créer
main.py
avec fonction main()
3
Premier commit : "Structure initiale"
4
Ajouter fonction
saluer(nom: str)
5
Second commit : "Ajout fonction saluer"
6
Vérifier avec
git log --oneline

def
saluer(nom: str) -> str:
"""Retourne un message de salutation."""
return f"Bonjour, {nom} !"

def
main():
print("Bienvenue!")
print(saluer("Utilisateur"))

Créer et Naviguer
$ git branch
Lister les branches
$ git branch feature-api
Créer une branche
$ git checkout feature-api
Basculer sur la branche
$ git checkout -b feature-api
✅ Créer ET basculer (raccourci)


Fusionner et Supprimer
$ git checkout main
Retourner sur main
$ git merge feature-api
Fusionner dans main
$ git branch -d feature-api
Supprimer (si fusionnée)
$ git branch -D feature-api
⚠️ Forcer suppression