import random
import time

def translateGame(wordsChapitre):
    option=""

    timeDelay = 0.3

    while option!="x":
        print(" ")
        print("Chapitre 1 : Le Survivant")
        print("1.- Traduis cela")
        print("2.- Afficher le dictionnaire")
        print("3.- Trouvez un mot")
        print(" ")
        option = input("Sélectionnez une option ou sortir(X): ")

        option.lower()

        if option=="1":

            #Size of the dictionary of french words for the Chapter 1
            sizeDict = len(wordsChapitre)

            #List with the keys of the dictionary
            listDictionary = list(wordsChapitre)

            print(sizeDict,"mots")

            #To count from 1 the words that have been correctly answered
            numberWords = 1

            while len(listDictionary) > 0:
                print("(",numberWords,"/",sizeDict,")")

                #Random number from 0 to sizeDict - 1
                randomWord = random.randrange(0,len(listDictionary))

                key = listDictionary[randomWord]

                #Prints a random word from the dictionary
                print(key)

                #The answer from the user
                answer = input()

                if isinstance(wordsChapitre[key], tuple):
                    if answer in wordsChapitre[key]:
                        print("C'est Correct!")
                        time.sleep(timeDelay)
                        print(" ")

                        #Remove from the dictionary list the key from the correct value
                        listDictionary.remove(key)

                        numberWords = numberWords + 1
                    else:
                        print("C'est incorrect")
                        print("The correct answer is: ",wordsChapitre[key])
                        time.sleep(timeDelay)
                        print(" ")

                #Check if the answer is the value of that word in the dictionary
                elif wordsChapitre[key] == answer:
                    print("C'est Correct!")
                    time.sleep(timeDelay)
                    print(" ")

                    #Remove from the dictionary list the key from the correct value
                    listDictionary.remove(key)

                    numberWords = numberWords + 1
                else:
                    print("C'est incorrect")
                    print("The correct answer is: ",wordsChapitre[key])
                    time.sleep(timeDelay)
                    print(" ")

            print(" ")
            print("Tu as traduit tous les mots!")
            print(" ")

        elif option=="2":
            print(" ")
            for x in wordsChapitre:
                print(x,": ",wordsChapitre[x])
            print(" ")
        elif option=="3":
            print("Entrez le mot: ")
            wordSearch = input()
            if wordSearch in wordsChapitre:
                print(wordsChapitre[wordSearch])
                time.sleep(3)
            else:
                print("Le mot n'est pas dans notre dictionnaire")
                time.sleep(2)
