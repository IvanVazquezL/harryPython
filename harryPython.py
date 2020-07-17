import random
from translate import translateGame

option = ""

while option != "x":
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

    option.lower()

    if option=="1":

        wordsChapitre1 = {
            "avoir": ("haber","tener"),
            "être" : "ser",
            "faire" : "hacer",
            "mots" : "palabras",
            "quiconque" : ("nadie","cualquiera","alguien"),
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
            "prochaine" : ("siguiente","próximo"),
            "sur" : ("en","sobre"),
            "loin" : "lejos",
            "robe" : ("vestido","tunica"),
            "emporter" : "llevar",
            "attendre" : "esperar",
            "baisser" : "beso",
            "cette" : "esta",
            "habitaient" : ("habitaban","vivían"),
            "avaient" : ("habían","tenían"),
            "toujours" : "siempre",
            "affirmé" : ("afirmado","asegurado"),
            "fierté" : "orgullo",
            "étaient": "eran",
            "aurait" : ("tendría","habría","hubiera"),
            "n'aurait" : ("no tendría","no habría","no hubiera"),
            "jamais" : ("jamas","nunca"),
            "puissent" : ("pueden","puede","poder","pueda"),
            "trouver" : "encontrar",
            "se trouver" : "encontrarse",
            "dans" : ("en","dentro","a","durante","a lo largo"),
            "quoi que ce soit" : "cualquier cosa",
            "n'avaient" : ("no tenían"),
            "sornettes" : ("tonterias","disparates"),
            "dirigeait" : "dirigía",
            "massif" : ("macizo","masivo","enorme"),
            "en revanche" : ("sin embargo","en cambio","por el contrario"),
            "n'avait" : "no tenía",
            "belle taille" : "buen tamaño",
            "quant à elle" : "en cuanto a ella",
            "était" : "era",
            "mince" : "delgada",
            "fort utile" : "muy útil",
            "en regardant" : "mirando",
            "par-dessus" : ("por arriba","encima","arriba"),
            "clôtures" : ("cercas","vallas"),
            "bel" : ("hermoso","bello"),
            "vouloir" : "querer",
            "voulaient" : ("querían","deseaban"),
            "dont" : ("el cual","cuyo"),
            "craignaient" : "temían",
            "qu'ils" : "que ellos",
            "si jamais" : "si alguna vez",
            "venait" : "venía",
            "convaincus" : "convencidos",
            "qu'ils ne s'en remettraient pas" : "que no se recuperarían",
            "sœur" : "hermana",
            "frère" : "hermano",
            "ne s'etaient plus revues" : "no se habían vuelto a ver",
            "années" : "años",
            "En fait" : "de hecho",
            "faisait" : "hacía",
            "fille" : ("hija","chica","muchacha","niña"),
            "fils" : ("niño","chico","muchacho","hijo"),
            "bon à rien" : "bueno para nada",
            "mari" : ("marido","esposo"),
            "aussi" : "también",
            "éloignés" : ("distante","lejano","remoto"),
            "aussi éloignés que possible" : ("tan lejanos como sea posible","tan lejos como sea posible","tan distantes entre sí como sea posible"),
            "de tout ce qui faisait" : "de todo lo que hacía",
            "qui" : ("que","quien"),
            "tremblaient" : "temblaban",
            "épouvante" : ("horror","terror"),
            "par malheur" : "por desgracia",
            "diraient" : "dirían",
            "montraient" : "mostraban",
            "leur" : "su",
            "rue" : "calle",
            "savaient" : "sabían",
            "eux aussi" : "también",
            "garçon" : ("niño","chico","joven"),
            "vu" : "visto",
            "supplémentaire" : ("suplementario","adicional"),
            "de tenir" : "de tener",
            "n'était pas question" : "estaba fuera de cuestión",
            "se mette" : ("se ponga","ponerse"),
            "mette" : ("poner","colocar","dejar"),
            "celui-là" : ("ese","aquel"),
            "lorsque" : "cuando",
            "s'éveillèrent" : "se despertaron",
            "il faisait" : "era",
            "nuageux" : "nublado",
            "ne laissait prévoir" : "no dejaba predecir",
            "allaient" : "iban",
            "bientôt" : "pronto",
            "fredonnait un air" : "tarareaba una melodía",
            "en nouant" : "atando",
            "cravate" : "corbata",
            "aller" : ("ir","vamos","andar"),
            "travailler" : "trabajar",
            "racontait" : ("estaba contando","estaba diciendo"),
            "un ton badin" : "un tono juguetón",
            "dernier" : "último",
            "potins" : "chismes",
            "quartier" : "barrio",
            "en s'efforçant" : "esforzándose",
            "jeune" : "joven",
            "mardi" : "martes",
            "jaune" : "amarillo",
            "braillat" : "gritaba"

        }

        translateGame(wordsChapitre1)
