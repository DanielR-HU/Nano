#Nano   Store



import time
import random
import os
# Check voor installatie pygame
try:
    import pygame.mixer
except ImportError:
    os.system("pip install pygame")
    import pygame.mixer

# Check voor installatie colorama
try:
    from colorama import init, Fore, Style
except ImportError:
    os.system("pip install colorama")
    from colorama import init, Fore, Style
init() # Dit zorgt er voor dat de kleuren werken
pygame.mixer.init()
ENDCOLOR = Style.RESET_ALL # Dit zorgt er voor dat de kleur weer naar normaal gaat
Ingelogd = False


def Clear():
    os.system('cls' if os.name == 'nt' else 'clear') # Dit zorgt er voor dat de console wordt leeg gemaakt

#Games\/\/\/\/
class Games:
    def CijferGuess():
        Clear()
        Cijfer_Graad = input("\t\t\tWelkom bij het cijfer guess spel!\n\n\t\tVul het cijfer in van de moeilijkeids graad die je wilt. \n\n\nWil je het makkelijk, normaal of moeilijk maken?\n 8 = makkelijk\n 4 = normaal\n 3 = moeilijk\n 1 = onmogelijk\n\n")
        if Cijfer_Graad.isdigit():
            Cijfer_Graad = int(Cijfer_Graad)
            if Cijfer_Graad == 1 or Cijfer_Graad == 3 or Cijfer_Graad == 4 or Cijfer_Graad == 8:
                Clear()
            else:
                print("Dit is geen geldige keuze")
                time.sleep(1)
                Games.CijferGuess()
        else:
            print("\nDit is geen nummer")
            time.sleep(1)
            Games.CijferGuess()

        aantal_guesses = 0
        nummer = random.randint(1, 10) # Maakt het random nummer

        while aantal_guesses < Cijfer_Graad: # Dit zorgt voor de hoeveelheid kansen die je hebt
            print(f"\n\nJe hebt gekozen voor {Cijfer_Graad} kansen om te raden\n")
            print(f"Je hebt {aantal_guesses} keer geraden\n")
            guess = input("Welk nummer tussen 1 en 10 denk je dat het is? \n")
            if guess.isnumeric():
                guess = int(guess) # Dit probeert de input om te zetten naar een integer
                if 1 <= guess <= 10: # Dit zorgt er voor dat het nummer tussen 1 en 10 is
                    aantal_guesses += 1 # Dit telt de aantal guesses op
                    if guess == nummer: # Dit zorgt er voor dat als je het nummer goed hebt geraden, dat het programma stopt
                        Clear()
                        print("\nGoed geraden!")
                        print(f"Je hebt het in {aantal_guesses} keer geraden\n")
                        terug = (input("Druk op enter om verder te gaan\n"))
                        if terug == "":
                            NanoStart()
                    elif guess < nummer: # Dit zorgt er voor dat als je het nummer fout hebt geraden, dat het programma zegt of het nummer hoger of lager is
                        Clear()
                        print(f"\n{guess} is te laag\n")
                        
                    else:
                        Clear()
                        print(f"\n{guess} is te hoog\n")
                else:
                    Clear()
                    print(f"\n{guess} is niet tussen 1 en 10")
            else:
                Clear()
                print(f"\n{guess} is geen nummer\n")

        if aantal_guesses == Cijfer_Graad and guess != nummer: # Dit zorgt er voor dat als je zo veel keer fout hebt geraden, dat het programma stopt en zegt wat het nummer was
            print("\nJe hebt het nummer niet geraden")
            print(f"Het nummer was {nummer}\n")
            terug = (input("Druk op enter om verder te gaan\n"))
            if terug == "":
                NanoStart()
    def Galgje():
        Clear()
        Usernname = input("Wat is je naam?\n")

        # Keuze van de woordenlijst
        Clear()
        Woordkeuze = input("\nWelke categorie wil je kiezen?\n1. Dieren\n2. Kleuren\n3. Voedsel\n")
        if Woordkeuze == "Dieren" or Woordkeuze == "dieren" or Woordkeuze == "1":
            WoordenlijstDieren = open("WoordenlijstDieren.txt", "r")   
            Woorden = WoordenlijstDieren.read()
            Woordenlijst = Woorden.replace('\n', ' ').split(",")
            print(Woordenlijst)
            WoordenlijstDieren.close()

        elif Woordkeuze == "Kleuren" or Woordkeuze == "kleuren" or Woordkeuze == "2":
            WoordenlijstKleuren = open("WoordenlijstKleuren.txt", "r")
            Woorden = WoordenlijstKleuren.read()
            Woordenlijst = Woorden.replace('\n', ' ').split(",")
            WoordenlijstKleuren.close()
        elif Woordkeuze == "Voedsel" or Woordkeuze == "voedsel" or Woordkeuze == "3":
            WoordenlijstVoedsel = open("WoordenlijstVoedsel.txt", "r")
            Woorden = WoordenlijstVoedsel.read()
            Woordenlijst = Woorden.replace('\n', ' ').split(",")
            WoordenlijstVoedsel.close()
        else:
            print("Dit is geen geldige keuze")
            Games.Galgje()                       
        
        
        Geraden = 0 #Boolean om te kijken of het woord is geraden
        Woord = Woordenlijst[random.randrange(0, len(Woordenlijst))] # Kiest een random woord uit de lijst
        Letters = list(str.lower(Woord)) # Maakt een lijst van de letters van het woord
        GeradenLetters = ['_' for _ in Letters] # Maakt een lijst van de letters van het woord, maar dan met underscores
        Fouten = 0 # Aantal fouten die je hebt gemaakt
        
        # Galg variabelen
        Clear()
        Galg1 = " =====\n |   ||\n     ||\n     ||\n     ||\n     ||\n     ||\n========\n"

        Galg2 = " =====\n |   ||\n O   ||\n     ||\n     ||\n     ||\n     ||\n========\n"

        Galg3 = " =====\n |   ||\n O   ||\n |   ||\n     ||\n     ||\n     ||\n========\n"

        Galg4 = " =====\n |   ||\n O   ||\n/|   ||\n     ||\n     ||\n     ||\n========\n"

        Galg5 = " =====\n |   ||\n O   ||\n/|\\  ||\n     ||\n     ||\n     ||\n========\n"

        Galg6 = " =====\n |   ||\n O   ||\n/|\\  ||\n  \\  ||\n     ||\n     ||\n========\n"

        Galg7 = " =====\n |   ||\n O   ||\n/|\\  ||\n/ \\  ||\n     ||\n     ||\n========\n"

        print(Galg1)
        # Loop voor het spel
        Galgfouten = Galg1
        while Geraden == 0:
            
            LetterGuess = input("geef een letter (Geen Woord): \n").lower()
            time.sleep(0.1)
            Clear()
            if LetterGuess in Letters:
                print(Galgfouten)
                print("\nJe hebt de letter goed\n")
                for i, letter in enumerate(Letters): # Enumerate zorgt er voor dat je de index en de waarde van de letter krijgt
                    if letter == LetterGuess:
                        GeradenLetters[i] = LetterGuess # Als de letter goed is, dan wordt de underscore vervangen door de letter
                print(str(GeradenLetters).replace("'", "").replace("[","").replace("]","").replace(",",""))
                if "_" not in GeradenLetters: # Als er geen underscores meer in de lijst zitten, dan is het woord geraden
                    Geraden = 1
                    
                    print("Je hebt het woord geraden!")
                    terug = (input("Druk op enter om verder te gaan\n"))
                    if terug == "":
                        NanoStart()

            else:
                Fouten += 1
                if Fouten < 6:
                    #De galg selector 5000TM
                    if Fouten == 1:
                        Galgfouten = Galg2
                    if Fouten == 2:
                        Galgfouten = Galg3
                    if Fouten == 3:
                        Galgfouten = Galg4
                    if Fouten == 4:
                        Galgfouten = Galg5
                    if Fouten == 5:
                        Galgfouten = Galg6
                    if Fouten == 6:
                        Galgfouten = Galg7
                    print(Galgfouten)
                else:
                    Galgfouten = Galg7
                    print(Galgfouten)
                    print("\nGame Over\n")
                    print("Het woord was: ", Woord)
                    terug = (input("\nDruk op enter om verder te gaan\n")) # Dit zorgt er voor dat je op enter moet drukken om verder te gaan naar het menu
                    if terug == "":
                        NanoStart()

                print("\nJe hebt de letter fout\n") # Als de letter fout is, dan wordt er een fout bij opgeteld
                print("Aantal fouten:", Fouten)
                print(str(GeradenLetters).replace("'", "").replace("[","").replace("]","").replace(",",""), "\n")
            if Fouten > 6:
                NanoStart()

    
    def GalgjeMultiplayer():
        Clear()
        print("Dit is de Multiplayer versie van Galgje")               
        
        
        Geraden = 0 #Boolean om te kijken of het woord is geraden
        Woord = input("Speler 1, voer een woord in Speler 2 niet kijken!: \n").replace(' ', '-')
        Letters = list(str.lower(Woord)) # Maakt een lijst van de letters van het woord
        GeradenLetters = ['_' for _ in Letters] # Maakt een lijst van de letters van het woord, maar dan met underscores
        Fouten = 0 # Aantal fouten die je hebt gemaakt
        GeradenLettersFix = str(GeradenLetters).replace("'", "").replace("[","").replace("]","").replace(",","")

        # Galg variabelen
        Clear()
        Galg1 = " =====\n |   ||\n     ||\n     ||\n     ||\n     ||\n     ||\n========\n"

        Galg2 = " =====\n |   ||\n O   ||\n     ||\n     ||\n     ||\n     ||\n========\n"

        Galg3 = " =====\n |   ||\n O   ||\n |   ||\n     ||\n     ||\n     ||\n========\n"

        Galg4 = " =====\n |   ||\n O   ||\n/|   ||\n     ||\n     ||\n     ||\n========\n"

        Galg5 = " =====\n |   ||\n O   ||\n/|\\  ||\n     ||\n     ||\n     ||\n========\n"

        Galg6 = " =====\n |   ||\n O   ||\n/|\\  ||\n  \\  ||\n     ||\n     ||\n========\n"

        Galg7 = " =====\n |   ||\n O   ||\n/|\\  ||\n/ \\  ||\n     ||\n     ||\n========\n"


        

        print(Galg1)
        print(GeradenLettersFix)
        # Loop voor het spel
        Galgfouten = Galg1
        while Geraden == 0:
            
        
            

            Spatie = '-'
            if Spatie in Letters:
                for i, letter in enumerate(Letters):
                    if letter == Spatie:
                        GeradenLetters[i] = Spatie


            LetterGuess = input("geef een letter (Geen Woord): \n").lower()
            time.sleep(0.1)
            Clear()
            if Fouten == 1:
                Galgfouten = Galg2
            if Fouten == 2:
                Galgfouten = Galg3
            if Fouten == 3:
                Galgfouten = Galg4
            if Fouten == 4:
                Galgfouten = Galg5
            if Fouten == 5:
                Galgfouten = Galg6
            if Fouten == 6:
                Galgfouten = Galg7


            if LetterGuess in Letters:
                print(Galgfouten)
                print("\nJe hebt de letter goed\n")
                for i, letter in enumerate(Letters): # Enumerate zorgt er voor dat je de index en de waarde van de letter krijgt
                    if letter == LetterGuess:
                        GeradenLetters[i] = LetterGuess # Als de letter goed is, dan wordt de underscore vervangen door de letter
                print(str(GeradenLetters).replace("'", "").replace("[","").replace("]","").replace(",",""))
                if "_" not in GeradenLetters: # Als er geen underscores meer in de lijst zitten, dan is het woord geraden
                    Geraden = 1
                    
                    print("Je hebt het woord geraden!")
                    terug = (input("Druk op enter om verder te gaan\n"))
                    if terug == "":
                        NanoStart()
            else:
                Fouten += 1
                if Fouten < 6:
                    
                    if Fouten == 1:
                        Galgfouten = Galg2
                    if Fouten == 2:
                        Galgfouten = Galg3
                    if Fouten == 3:
                        Galgfouten = Galg4
                    if Fouten == 4:
                        Galgfouten = Galg5
                    if Fouten == 5:
                        Galgfouten = Galg6
                    if Fouten == 6:
                        Galgfouten = Galg7
                    print(Galgfouten)
                else:
                    Galgfouten = Galg7
                    print(Galgfouten)
                    print("\nGame Over\n")
                    print("Het woord was: ", Woord)
                    terug = (input("\nDruk op enter om verder te gaan\n")) # Dit zorgt er voor dat je op enter moet drukken om verder te gaan naar het menu
                    if terug == "":
                        NanoStart()

                print("\nJe hebt de letter fout\n") # Als de letter fout is, dan wordt er een fout bij opgeteld
                print("Aantal fouten:", Fouten)
                print(str(GeradenLetters).replace("'", "").replace("[","").replace("]","").replace(",",""), "\n")

            
            if Fouten > 6:
                NanoStart()

        
                                                                    

                                                      


#UI \/\/\/\/
class UI:
    def Welkom():
        Clear()
        print(Fore.GREEN + "$$\\   $$\\                                      $$$$$$\\  $$\\                           ")
        time.sleep(0.1)
        print( "$$$\\  $$ |                                    $$  __$$\\ $$ |                          ")
        time.sleep(0.1)
        print( "$$$$\\ $$ | $$$$$$\\  $$$$$$$\\   $$$$$$\\        $$ /  \\__|$$$$$$$\\   $$$$$$\\   $$$$$$\\  ")
        time.sleep(0.1)
        print( "$$ $$\\$$ | \\____$$\\ $$  __$$\\ $$  __$$\\       \\$$$$$$\\  $$  __$$\\ $$  __$$\\ $$  __$$\\ ")
        time.sleep(0.1)
        print( "$$ \\$$$$ | $$$$$$$ |$$ |  $$ |$$ /  $$ |       \\____$$\\ $$ |  $$ |$$ /  $$ |$$ /  $$ |")
        time.sleep(0.1)
        print( "$$ |\\$$$ |$$  __$$ |$$ |  $$ |$$ |  $$ |      $$\\   $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |")
        time.sleep(0.1)
        print( "$$ | \\$$ |\\$$$$$$$ |$$ |  $$ |\\$$$$$$  |      \\$$$$$$  |$$ |  $$ |\\$$$$$$  |$$$$$$$  |")
        time.sleep(0.1)
        print( "\\__|  \\__| \\_______|\\__|  \\__| \\______/        \\______/ \\__|  \\__| \\______/ $$  ____/ ")
        time.sleep(0.1)
        print( "                                                                            $$ |      ")
        time.sleep(0.1)
        print( "                                                                            $$ |      ")
        time.sleep(0.1)
        print( "                                                                            \\__|      " + ENDCOLOR)
        time.sleep(0.1)
    
    
    def Selector():
        if Ingelogd == True:
            print("Kies uw spel:")
            print("1. Cijfer guesser")
            print("2. Galgje")
            print("3. Galgje Multiplayer")
            keuze = input("\nVoer het nummer van het spel in:\n ")
            if keuze.isdigit():
                keuze = int(keuze)
                if keuze == 1:
                    Games.CijferGuess()
                elif keuze == 2:
                    Games.Galgje()
                elif keuze == 3:
                    Games.GalgjeMultiplayer()
            else:
                print("Dit is geen geldige keuze")
                time.sleep(1)
                NanoStart()
        else:
            print("Wilt u registreren of inloggen?")
            print("1. Registreren")
            print("2. Inloggen")
            keuze = input("\nVoer het nummer van de keuze in:\n ")
            if keuze.isdigit():
                keuze = int(keuze)
                if keuze == 1:
                    UI.Registreren()
                elif keuze == 2:
                    UI.Inloggen()
            else:
                print("Dit is geen geldige keuze")
                time.sleep(1)
                NanoStart()

def NanoStart():
    UI.Welkom()
    UI.Selector()

NanoStart()