import random
from translate import translateGame

option = ""

while option != "X":
    print(" ")
    print("Harry Potter à l'école des sorciers")
    print("par J.K. Rowling")
    print(" ")
    print("Pour Jessica, qui adore les histoires,")
    print("pour Anne, qui les adorait aussi,")
    print("et pour Di, qui a été la première à entendre celle-ci.")
    print(" ")
    print("Liste des chapitres")
    print("Chapitre 1 : Le Survivant")
    print("Chapitre 2 : Une Vitre Disparaît")
    print("Chapitre 3 : Les Lettres de Nulle Part")
    print("Chapitre 4 : Le Gardien des Clés")
    print("Chapitre 5 : Le Chemin de Traverse")
    print("Chapitre 6 : Rendez – Vous sur la Voie 9 3/4")
    print("Chapitre 7 : Le Choixpeau Magique")
    print("Chapitre 8 : Le Maître des Potions")
    print("Chapitre 9 : Duel à Minuit")
    print("Chapitre 10 : Halloween")
    print("Chapitre 11 : Le Match de Quidditch")
    print("Chapitre 12 : Le Miroir de Riséd")
    print("Chapitre 13 : Nicolas Flamel")
    print("Chapitre 14 : Norbert le Dragon")
    print("Chapitre 15 : La Forêt Interdite")
    print("Chapitre 16 : Sous la Trappe")
    print("Chapitre 17 : L’ Homme aux Deux Visages")
    print(" ")
    option = input("Sélectionnez un chapitre ou sortir(X): ")

    if option=="1":

        wordsChapitre1 = {
            "avoir": ("haber","tener"),
            "être" : "ser",
            "faire" : "hacer",
            "mots" : "palabras",
            "quiconque" : "nadie",
            "pendant" : "durante",
            "parfois" : "a veces",
            "blessé" : "herido",
            "presque" : "casi",
            "jusqu'a" : "hasta",
            "quelque chose" : "algo",
            "perceuses" : "taladros",
            "leurs" : "sus",
            "depuis" : "desde",
            "car" : "porque",
            "entendre" : "escuchar",
            "toutes deux" : "ambos",
            "chaise" : "silla",
            "jeter" : ("tirar","lanzar","echar","arrojar"),
            "assis" : "sentado",
            "tandis" : "mientras",
            "commande" : "pedido",
            "beignet" : ("rosquilla","dona"),
            "vers" : "hacia",
            "boutique" : "tienda",
            "avant" : "antes",
            "cet" : "este",
            "temps" : ("tiempo","clima"),
            "prochaine" : ("siguiente","proximo"),
            "sur" : ("en","sobre"),
            "loin" : "lejos",
            "robe" : ("vestido","tunica"),
            "emporter" : "llevar",
            "attendre" : "esperar",
            "baisser" : "beso",
            "cette" : "esta"
        }

        translateGame(wordsChapitre1)
