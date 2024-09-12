#NanoStartStore
#pip install colorama

import time
import random
import os
from colorama import init, Fore, Style

os.system("pip install colorama") # Dit zorgt er voor dat de colorama module wordt geinstalleerd
init() # Dit zorgt er voor dat de kleuren werken


ENDCOLOR = Style.RESET_ALL # Dit zorgt er voor dat de kleur weer naar normaal gaat
LineBreak = "\n"*30 # Dit zorgt er voor dat de console wordt leeg gemaakt soort van

#Games\/\/\/\/
class Games:
    def CijferGuess():
        print(LineBreak)
        Cijfer_Graad = input("Welkom bij het cijfer guess spel!\nVul het cijfer in van de moeilijkeids graad die je wilt. \nWil je het makkelijk, normaal of moeilijk maken?\nmakkelijk = 8\nnormaal = 4\nmoeilijk = 3\nonmogelijk = 1\n")
        try:
            Cijfer_Graad = int(Cijfer_Graad)
            if Cijfer_Graad == 1 or Cijfer_Graad == 3 or Cijfer_Graad == 4 or Cijfer_Graad == 8:
                print("Je hebt gekozen voor", Cijfer_Graad, "kansen om te raden")
            else:
                print("Dit is geen geldige keuze")
                Games.CijferGuess()
        except ValueError:
            print("Dit is geen nummer")
            Games.CijferGuess()

        aantal_guesses = 0
        nummer = random.randint(1, 10) # Maakt het random nummer

        while aantal_guesses < Cijfer_Graad: # Dit zorgt voor de hoeveelheid kansen die je hebt
            guess = input("Welk nummer tussen 1 en 10 denk je dat het is? \n")
            try: # Dit zorgt er voor dat als je geen nummer invoert, dat je het opnieuw kan proberen.
                guess = int(guess) # Dit probeert de input om te zetten naar een integer
                if 1 <= guess <= 10: # Dit zorgt er voor dat het nummer tussen 1 en 10 is
                    aantal_guesses += 1 # Dit telt de aantal guesses op
                    if guess == nummer: # Dit zorgt er voor dat als je het nummer goed hebt geraden, dat het programma stopt
                        print("\nGoed geraden!")
                        print("Je hebt het in", aantal_guesses, "keer geraden\n")
                        terug = (input("Druk op enter om verder te gaan\n"))
                        if terug == "":
                            NanoStart()
                    elif guess < nummer: # Dit zorgt er voor dat als je het nummer fout hebt geraden, dat het programma zegt of het nummer hoger of lager is
                        print("\nTe laag\n")
                    else:
                        print("\nTe hoog\n")
                else:
                    print("\nDit nummer is niet tussen 1 en 10")
            except ValueError:
                print("\nDit is geen nummer\n")

        if aantal_guesses == Cijfer_Graad and guess != nummer: # Dit zorgt er voor dat als je zo veel keer fout hebt geraden, dat het programma stopt en zegt wat het nummer was
            print("\nJe hebt het nummer niet geraden")
            print("Het nummer was", nummer, "\n")
            terug = (input("Druk op enter om verder te gaan\n"))
            if terug == "":
                NanoStart()
    def Galgje():
        WoordenlijstDieren = ["Kat", "Hond", "Vis", "Rat", "Bij", "Uil", "Kip", "Mug", "Eek", "Vos"]
        WoordenlijstKleuren = ["Rood", "Blauw", "Geel", "Groen", "Roze", "Paars", "Grijs", "Zwart", "Wit", "Cyaan"]
        WoordenlijstVoedsel = ["Appel", "Peer", "Brood", "Ei", "Melk", "Kaas", "Soep", "Rijst", "Vis", "Kip"]
       
        Woordkeuze = input("Welke categorie wil je kiezen?\n1. Dieren\n2. Kleuren\n3. Voedsel\n")
        if Woordkeuze == "Dieren" or Woordkeuze == "dieren" or Woordkeuze == "1":
            Woordenlijst = WoordenlijstDieren
        elif Woordkeuze == "Kleuren" or Woordkeuze == "kleuren" or Woordkeuze == "2":
            Woordenlijst = WoordenlijstKleuren
        elif Woordkeuze == "Voedsel" or Woordkeuze == "voedsel" or Woordkeuze == "3":
            Woordenlijst = WoordenlijstVoedsel
        else:
            print("Dit is geen geldige keuze")
            Games.Galgje()                       
        
        
        
        Geraden = 0
        Woord = Woordenlijst[random.randrange(0, len(Woordenlijst))]
        Letters = list(str.lower(Woord))
        GeradenLetters = ["_" for _ in Letters]
        Fouten = 0


        print(LineBreak)

        print(" =====")
        print(" |   ||")
        print("     ||")
        print("     ||")
        print("     ||")
        print("     ||")
        print("     ||")
        print(" ========")
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
                    print("Je hebt het woord geraden!")
                    terug = (input("Druk op enter om verder te gaan\n"))
                    if terug == "":
                        NanoStart()

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
                terug = (input("Druk op enter om verder te gaan\n"))
                if terug == "":
                    NanoStart()
            if Fouten > 6:
                NanoStart()

#UI \/\/\/\/
class UI:
    def Welkom():
        
        print(LineBreak)
        print(Fore.GREEN + "$$\   $$\                                      $$$$$$\  $$\                           ")
        time.sleep(0.1)
        print( "$$$\  $$ |                                    $$  __$$\ $$ |                          ")
        time.sleep(0.1)
        print( "$$$$\ $$ | $$$$$$\  $$$$$$$\   $$$$$$\        $$ /  \__|$$$$$$$\   $$$$$$\   $$$$$$\  ")
        time.sleep(0.1)
        print( "$$ $$\$$ | \____$$\ $$  __$$\ $$  __$$\       \$$$$$$\  $$  __$$\ $$  __$$\ $$  __$$\ ")
        time.sleep(0.1)
        print( "$$ \$$$$ | $$$$$$$ |$$ |  $$ |$$ /  $$ |       \____$$\ $$ |  $$ |$$ /  $$ |$$ /  $$ |")
        time.sleep(0.1)
        print( "$$ |\$$$ |$$  __$$ |$$ |  $$ |$$ |  $$ |      $$\   $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |")
        time.sleep(0.1)
        print( "$$ | \$$ |\$$$$$$$ |$$ |  $$ |\$$$$$$  |      \$$$$$$  |$$ |  $$ |\$$$$$$  |$$$$$$$  |")
        time.sleep(0.1)
        print( "\__|  \__| \_______|\__|  \__| \______/        \______/ \__|  \__| \______/ $$  ____/ ")
        time.sleep(0.1)
        print( "                                                                            $$ |      ")
        time.sleep(0.1)
        print( "                                                                            $$ |      ")
        time.sleep(0.1)
        print( "                                                                            \__|      " + ENDCOLOR)
        time.sleep(0.1)
        
    def Selector():
        print("Kies uw spel:")
        print("1. Cijfer guesser")
        print("2. Galgje")
        keuze = int(input("\nVoer het nummer van het spel in:\n "))
        if keuze == 1:
            Games.CijferGuess()
        elif keuze == 2:
            Games.Galgje()

def NanoStart():
    UI.Welkom()
    UI.Selector()

NanoStart()