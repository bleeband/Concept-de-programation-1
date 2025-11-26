
#  CHAINE DE CARACTERE

# une_str = "Je suis une chaine de caracteres !"
# une_str2 = str("Je suis une chaine de caracteres !")
# une_str3 = str([0, "il faait beau", True, 1.2])

# print(une_str)
# print(une_str2)
# print(une_str3)

# # \n  -->  saut de ligne
# # \t  -->  ajout dune tabulation (8 caracteres)
# # \r  -->  

# print("je suis un merveilleux paragraphe \nEn voici la preuve")

# print("voici le profil : \n\tNom : Lilia \n\tAge : 41ans")

# print("aujourdhui il fait beau \rau fait il fait beau")

# # '' ou ""

# un_paragraphe = 'le contenu de mon paragraphe, c\'est le texte'
# un_paragraphe1 = "le contenu de mon paragraphe, c'est le texte"
# un_paragraphe2 = "voici le texte d'un paragraphe" \
# "voici le saut"
# un_paragraphe3 = "voici le texte d'un paragraphe \n"
# "voici le saut"
# un_paragraphe4 = """voici le texte d'un paragraphe
# voici le saut"""

# print(un_paragraphe)
# print(un_paragraphe1)
# print(un_paragraphe2)
# print(un_paragraphe3)
# print(un_paragraphe4)

# nom = "marc"
# age = 41

# print("bonjour, votre nom est " + nom + ".\nVotre age est : " + str(age) + "ans")

# nom_livre = "harry potter 1"
# auteur_livre = "j.k. rowling"
# annee_publi = "2028"

# un_livre = f"""
# le nom du livre : {nom_livre}
# le nom de l'auteur : {auteur_livre}
# l'année de publi : {annee_publi}
# """

# print(un_livre)

# INDEXES DES CHAINES DE CARACTERES []

# a = "Les cours sont en ligne sur GitHub!"
# print(a[4])
# print(a[-1])
# print(a[-5])

# print(a[0:3])
# print(a[4:9])
# print(a[:9])
# print(a[9:])
# print(a[10: 23: 2])
# #[x : y : z]    [Départ : Fin : Bond]

# print(a[-5: :-1])
# print(a[-1: :-1])

#  LEN() et les methodes pour les chaines de caractere

# len
# capitaliza
# title
# upper
# lower
# count
# find
# index
# endswitch
# startswith

# chaine = "on est Lundi !"
# print(len(chaine))
# print(chaine.capitalize())
# print(chaine.title())
# print(chaine.upper())
# print(chaine.lower())

# print("Je suis malade" == "je suis malade")
# print("Je suis malade".lower() == "je suis malade".lower())

# print(chaine.count("n"))
# print(chaine.count("n", 5))

# print(chaine.index("t"))
# print(chaine.lower().index("lundi".lower()))

# print(chaine.endswith("."))
# print(chaine.startswith("o"))


#  AUTRES METHODES

# split
# splitlines
# join
# replace
# removeprefix
# removesuffix

chaine = "Je suis une pomme"

# result = chaine.split()
# print(result)
# print(chaine.split("suis"))
# print(chaine.split(" ", 1))

paragraphe = """Je suis
une paragraphe 
sur plusieurs
lignes !!!"""

print(paragraphe.splitlines())
print(paragraphe.splitlines(True))
print(chaine.join(["1. ", "2. ", "3. "]))

print(chaine.replace("e", "E", 2))

test = "[DB] Je suis un test [DB]"

print(test.removeprefix("[DB]"))
print(test.removesuffix("[DB]"))
print(test.removeprefix("[DB]").removesuffix("[DB]"))
