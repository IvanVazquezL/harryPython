import random
import time

def translateGame(wordsChapitre):
    option=""

    while option!="X":
        print(" ")
        print("Chapitre 1 : Le Survivant")
        print("1.- Traduis cela")
        print("2.- Afficher le dictionnaire")
        print(" ")
        option = input("Sélectionnez une option ou sortir(X): ")

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
                        time.sleep(0.5)
                        print(" ")

                        #Remove from the dictionary list the key from the correct value
                        listDictionary.remove(key)

                        numberWords = numberWords + 1
                    else:
                        print("C'est incorrect")
                        print("The correct answer is: ",wordsChapitre[key])
                        time.sleep(0.5)
                        print(" ")

                #Check if the answer is the value of that word in the dictionary
                elif wordsChapitre[key] == answer:
                    print("C'est Correct!")
                    time.sleep(0.5)
                    print(" ")

                    #Remove from the dictionary list the key from the correct value
                    listDictionary.remove(key)

                    numberWords = numberWords + 1
                else:
                    print("C'est incorrect")
                    print("The correct answer is: ",wordsChapitre[key])
                    time.sleep(0.5)
                    print(" ")

            print(" ")
            print("Tu as traduit tous les mots!")
            print(" ")

        elif option=="2":
            print(" ")
            for x in wordsChapitre:
                print(x,": ",wordsChapitre[x])
            print(" ")
