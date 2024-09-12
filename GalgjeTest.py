#Galgje

import random

Woordenlijst = ["Auto", "Boom", "Huis", "Hond", "Kat", "Maan", "Ster", "Vis", "Boek", "Tafel", "Stoel", "Fiets", "Vliegtuig", "Trein", "Appel", "Banaan", "Brood", "Melk", "Water", "Kaas", "Jas", "Schoen", "Hoed", "Muur", "Deur"]
Geraden = 0
Woord = Woordenlijst[random.randrange(0, len(Woordenlijst))]
Letters = list(str.lower(Woord))
GeradenLetters = ["_" for _ in Letters]
Fouten = 0


print(LineBreak)


while Geraden == 0:
    
    LetterGuess = input("geef een letter: \n").lower()
    if LetterGuess in Letters:
        print("\ngoed\n")
        for i, letter in enumerate(Letters):
            if letter == LetterGuess:
                GeradenLetters[i] = LetterGuess
        print(GeradenLetters)
        if "_" not in GeradenLetters:
            Geraden = 1
            print("GOEDZOOOO")
            break

    else:
        print("\nfout\n")
        Fouten += 1
        print("Aantal fouten:", Fouten)
        print(GeradenLetters, "\n")

    if Fouten == 0:
        print(" =====")
        print(" |   ||")
        print("     ||")
        print("     ||")
        print("     ||")
        print("     ||")
        print("     ||")
        print(" ========")
    if Fouten == 1:
        print(" =====")
        print(" |   ||")
        print(" O   ||")
        print("     ||")
        print("     ||")
        print("     ||")
        print("     ||")
        print(" ========")
    if Fouten == 2:
        print(" =====")
        print(" |   ||")
        print(" O   ||")
        print(" |   ||")
        print("     ||")
        print("     ||")
        print("     ||")
        print(" ========")
    if Fouten == 3:
        print(" =====")
        print(" |   ||")
        print(" O   ||")
        print("/|   ||")
        print("     ||")
        print("     ||")
        print("     ||")
        print(" ========")
    if Fouten == 4:
        print(" =====")
        print(" |   ||")
        print(" O   ||")
        print("/|\  ||")
        print("     ||")
        print("     ||")
        print("     ||")
        print(" ========")
    if Fouten == 5:
        print(" =====")
        print(" |   ||")
        print(" O   ||")
        print("/|\  ||")
        print("  \  ||")
        print("     ||")
        print("     ||")
        print(" ========")    
    if Fouten == 6:
        print(" =====")
        print(" |   ||")
        print(" O   ||")
        print("/|\  ||")
        print("/ \  ||")
        print("     ||")
        print("     ||")
        print(" ========")
        print(" ")
        print("Game Over")
        print("Het woord was: ", Woord)
        break
    
  