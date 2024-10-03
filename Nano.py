#nano 2.0

import time
import random
import os
import datetime
import requests
import tkinter as tk

#main functies

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def inloggen():
    clear()
    print("Welkom bij Nano\n")
    print("Log in om verder te gaan")
    print("Gebruikersnaam:")
    username = input("> ")
    print("\nWachtwoord:")
    password = input("> ")
    with open("users.txt", "r") as file:
        for line in file:
            user, pw = line.strip().split(",")
            if user == username and pw == password:
                clear()
                print(f"Welkom {username}")
                time.sleep(1)
                return username
            else:
                print("Gebruikersnaam of wachtwoord is fout")
                time.sleep(1)
                return AccountPagina()
        print("Gebruikersnaam of wachtwoord is fout")

def registreren():
    clear()
    print("Welkom bij Nano\n")
    print("Registreer uw account")
    print("Gebruikersnaam:")
    username = input(">")
    print("\nWachtwoord:")
    password = input(">")
    with open("users.txt", "a") as file:
        file.write(username + "," + password + "\n")
    clear()
    print("Account gemaakt")
    time.sleep(1)
    return AccountPagina()

def AccountPagina():
    clear()
    print("Inlog pagina\n")
    keuze = input("1. Inloggen\n2. Registreren\n\n> ")
    if keuze == "1":
        username = inloggen()
        return username
    elif keuze == "2":
        registreren()
    else:
        print("Foute invoer")
        time.sleep(1)
        AccountPagina()

def AppPagina(username):
    clear()
    print("Welkom bij Nano\n")
    print("Kies een app:")
    print("1. CijferGuess\n2. Galgje\n3. Galgje log\n4. Boter kaas en eieren (GUI)\n5. Het weer\n6. Exit\n")
    keuze = input("> ")
    if keuze == "1":
        CijferGuess(username)
    elif keuze == "2":
        Galgje(username)
    elif keuze == "3":
        GalgjeLog(username)
    elif keuze == "4":
        BoterKaasEieren(username)
    elif keuze == "5":
        HetWeer(username)
    elif keuze == "6":
        exit()
    else:
        print("Foute invoer")
        time.sleep(1)
        AppPagina(username)

def CijferGuess(username):
    highscore = 0
    with open("HighscoreCijfer.txt", "r") as file:
        for line in file:
            user, highscoreL = line.strip().split(",")
            if user == username:
                highscore = highscoreL
                break
    clear()
    Cijfer_Graad = input(f"\t\t\tWelkom bij het cijfer guess spel {username}!\n\t\t\t   --------Je highscore is {highscore}--------\n\n\t\tVul het cijfer in van de moeilijkeids graad die je wilt. \n\n\nWil je het makkelijk, normaal of moeilijk maken?\n 8 = makkelijk\n 4 = normaal\n 3 = moeilijk\n 1 = onmogelijk\n\n> ")
    if Cijfer_Graad.isdigit():
        Cijfer_Graad = int(Cijfer_Graad)
        if Cijfer_Graad == 1 or Cijfer_Graad == 3 or Cijfer_Graad == 4 or Cijfer_Graad == 8:
            clear()
        else:
            print("Dit is geen geldige keuze")
            time.sleep(1)
            CijferGuess()
    else:
        print("\nDit is geen nummer")
        time.sleep(1)
        CijferGuess()

    aantal_guesses = 0
    aantal_guesses = int(aantal_guesses)
    nummer = random.randint(1, 10) # Maakt het random nummer

    while aantal_guesses < Cijfer_Graad: # Dit zorgt voor de hoeveelheid kansen die je hebt
        print(f"\n\nJe hebt gekozen voor {Cijfer_Graad} kansen om te raden\n")
        print(f"Je hebt {aantal_guesses} keer geraden\n")
        guess = input("Welk nummer tussen 1 en 10 denk je dat het is? \n\n> ")
        if guess.isnumeric():
            guess = int(guess) # Dit probeert de input om te zetten naar een integer
            if 1 <= guess <= 10: # Dit zorgt er voor dat het nummer tussen 1 en 10 is
                aantal_guesses += 1 # Dit telt de aantal guesses op
                if guess == nummer: # Dit zorgt er voor dat als je het nummer goed hebt geraden, dat het programma stopt
                    clear()
                    print("\nGoed geraden!")
                    print(f"Je hebt het in {aantal_guesses} keer geraden\n")
                    with open("HighscoreCijfer.txt", "r") as file:
                        lines = file.readlines()
                        lines.remove(f"{username},{highscore}\n")
                    with open("HighscoreCijfer.txt", "w") as file:
                        lines.append(f"{username},{aantal_guesses}\n")
                        file.writelines(lines)
                    terug = (input("Druk op enter om verder te gaan\n"))
                    if terug == "":
                        AppPagina(username)
                elif guess < nummer: # Dit zorgt er voor dat als je het nummer fout hebt geraden, dat het programma zegt of het nummer hoger of lager is
                    clear()
                    print(f"\n{guess} is te laag\n")
                else:
                    clear()
                    print(f"\n{guess} is te hoog\n")
            else:
                clear()
                print(f"\n{guess} is niet tussen 1 en 10")
        else:
            clear()
            print(f"\n{guess} is geen nummer\n")

    if aantal_guesses == Cijfer_Graad and guess != nummer: # Dit zorgt er voor dat als je zo veel keer fout hebt geraden, dat het programma stopt en zegt wat het nummer was
        print("\nJe hebt het nummer niet geraden")
        print(f"Het nummer was {nummer}\n")
        terug = (input("Druk op enter om verder te gaan\n"))
        if terug == "":
            AppPagina(username)

def Galgje(username):
        # Keuze van de woordenlijst
        clear()
        Woordkeuze = input("\nHoe lastig wil je de woorden hebben?\n1. Makkelijk\n2. Normaal\n3. Moeilijk\n\n>")
        if Woordkeuze == "Makkelijk" or Woordkeuze == "makkelijk" or Woordkeuze == "1":
            with open("WoordenlijstMakkelijk.txt", "r") as WoordenlijstMakkelijk:
                Woordenlijst = WoordenlijstMakkelijk.read().splitlines()
        elif Woordkeuze == "Normaal" or Woordkeuze == "normaal" or Woordkeuze == "2":
           with open("WoordenlijstNormaal.txt", "r") as WoordenlijstNormaal:
                Woordenlijst = WoordenlijstNormaal.read().splitlines()
        elif Woordkeuze == "Moeilijk" or Woordkeuze == "moeilijk" or Woordkeuze == "3":
            with open("WoordenlijstMoeilijk.txt", "r") as WoordenlijstMoeilijk:
                Woordenlijst = WoordenlijstMoeilijk.read().splitlines()
        else:
            print("Dit is geen geldige keuze")
            Galgje()                       
        
        
        Geraden = 0 #Boolean om te kijken of het woord is geraden
        Woord = Woordenlijst[random.randrange(0, len(Woordenlijst))] # Kiest een random woord uit de lijst
        Letters = list(str.lower(Woord)) # Maakt een lijst van de letters van het woord
        GeradenLetters = ['_' for _ in Letters] # Maakt een lijst van de letters van het woord, maar dan met underscores
        Fouten = 0 # Aantal fouten die je hebt gemaakt
        
        # Galg variabelen
        clear()
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
        print(str(GeradenLetters).replace("'", "").replace("[","").replace("]","").replace(",",""))
        while Geraden == 0:
            
            LetterGuess = input("geef een letter (Geen Woord): \n\n>").lower()
            time.sleep(0.1)
            clear()
            if LetterGuess in Letters:
                print(Galgfouten)
                print("\nJe hebt de letter goed\n")
                for i, letter in enumerate(Letters): # Enumerate zorgt er voor dat je de index en de waarde van de letter krijgt
                    if letter == LetterGuess:
                        GeradenLetters[i] = LetterGuess # Als de letter goed is, dan wordt de underscore vervangen door de letter
                print(str(GeradenLetters).replace("'", "").replace("[","").replace("]","").replace(",",""))
                if "_" not in GeradenLetters: # Als er geen underscores meer in de lijst zitten, dan is het woord geraden
                    Geraden = 1
                    #GERADEN!!!!
                    datum = datetime.datetime.now()
                    with open("LogGalgje.txt", "a") as file:
                        file.write(f"{username} heeft het woord {Woord} geraden met {Fouten} fouten op {datum}\n")
                    print("Je hebt het woord geraden!")
                    terug = (input("Druk op enter om verder te gaan\n"))
                    if terug == "":
                        AppPagina(username)

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
                        AppPagina(username)

                print("\nJe hebt de letter fout\n") # Als de letter fout is, dan wordt er een fout bij opgeteld
                print("Aantal fouten:", Fouten)
                print(str(GeradenLetters).replace("'", "").replace("[","").replace("]","").replace(",",""), "\n")
            if Fouten > 6:
                AppPagina(username)

def GalgjeLog(username):
    clear()
    with open("LogGalgje.txt", "r") as file:
        for line in file:
            print(line)
    terug = (input("Druk op enter om verder te gaan\n"))
    if terug == "":
        AppPagina(username)

def BoterKaasEieren(username):
    root = tk.Tk() # Dit maakt een tkinter window aan
    root.title("Boter, Kaas en Eieren") # Dit zorgt er voor dat de titel van het window "Boter, Kaas en Eieren" is

    speler = "X"
    bord = [["" for _ in range(3)] for _ in range(3)]
    def switch_player(): 
        nonlocal speler # Dit zorgt er voor dat de speler variabele global is omdat het niet anders kan
        speler = "O" if speler == "X" else "X"
        return speler
    
    def check_winnaar():
        # Horizontaal check
        for rij in bord:
            if rij[0] == rij[1] == rij[2] != "": #check of 1 2 3 van de rijen hetzelfde zijn en niet leeg
                return True
        # Verticaal check
        for kolom in range(3):
            if bord[0][kolom] == bord[1][kolom] == bord[2][kolom] != "": #hetzelfde als eerst maar dan verticaal
                return True
        # Diagonaal check
        if bord[0][0] == bord[1][1] == bord[2][2] != "": #Hetzelfde hier ook maar dan diagonaal
            return True
        if bord[0][2] == bord[1][1] == bord[2][0] != "":
            return True
        return False

    def button_click(button, k, rij, kolom):
        if bord[rij][kolom] == "": #als het vakje leeg is
            bord[rij][kolom] = speler #zet de speler icoon in het vakje bij het 2d bord
            k.set(speler) #zet de speler icoon in de button
            if check_winnaar():
                clear()
                print(f"{speler} heeft gewonnen!")
                root.destroy()
            switch_player()

    k1_1 = tk.StringVar() #tk.StringVar() is een variabele die je kan gebruiken in een tkinter window
    k1_2 = tk.StringVar() #tk.StringVar() zorgt er voor dat je de tekst van de button kan veranderen
    k1_3 = tk.StringVar() #simpel uitgelegd werkt het zo: als je de variabele veranderd, veranderd de tekst van de button ook
    k2_1 = tk.StringVar()
    k2_2 = tk.StringVar()
    k2_3 = tk.StringVar()
    k3_1 = tk.StringVar()
    k3_2 = tk.StringVar()
    k3_3 = tk.StringVar()

    button1_1 = tk.Button(root, textvariable=k1_1, width=10, height=5, command=lambda: button_click(button1_1, k1_1, 0, 0)) # Dit maakt een button aan met de waarde van de variabele k1_1 hetzelfde met die er onder.
    button1_1.grid(row = 0, column = 0)
    
    button1_2 = tk.Button(root, textvariable=k1_2, width=10, height=5, command=lambda: button_click(button1_2, k1_2, 0, 1)) # de nummers 0 en 1 zijn de rij en kolom van het bord voor het 2d bord
    button1_2.grid(row=0, column=1)

    button1_3 = tk.Button(root, textvariable=k1_3, width=10, height=5, command=lambda: button_click(button1_3, k1_3, 0, 2)) #button1_3 laat weten welke button het is en k1_3 laat weten welke variabele het is
    button1_3.grid(row=0, column=2)

    button2_1 = tk.Button(root, textvariable=k2_1, width=10, height=5, command=lambda: button_click(button2_1, k2_1, 1, 0)) #Lambda zorgt er voor dat de button_click functie wordt uitgevoerd met de juiste parameters
    button2_1.grid(row=1, column=0)

    button2_2 = tk.Button(root, textvariable=k2_2, width=10, height=5, command=lambda: button_click(button2_2, k2_2, 1, 1))
    button2_2.grid(row=1, column=1)

    button2_3 = tk.Button(root, textvariable=k2_3, width=10, height=5, command=lambda: button_click(button2_3, k2_3, 1, 2))
    button2_3.grid(row=1, column=2)

    button3_1 = tk.Button(root, textvariable=k3_1, width=10, height=5, command=lambda: button_click(button3_1, k3_1, 2, 0))
    button3_1.grid(row=2, column=0)

    button3_2 = tk.Button(root, textvariable=k3_2, width=10, height=5, command=lambda: button_click(button3_2, k3_2, 2, 1))
    button3_2.grid(row=2, column=1)

    button3_3 = tk.Button(root, textvariable=k3_3, width=10, height=5, command=lambda: button_click(button3_3, k3_3, 2, 2))
    button3_3.grid(row=2, column=2)
    
    root.mainloop() # Dit zorgt er voor dat het window blijft draaien
    terug = (input("Druk op enter om verder te gaan\n"))
    if terug == "":
        AppPagina(username)

def HetWeer(username):
    clear()

    countryCode = "NL" # Er is een country code nodig dus NL
    city = input("Voer stad in: ")

    locationKey = requests.get(f"http://dataservice.accuweather.com/locations/v1/cities/{countryCode}/search?apikey=NCkXL1pFDKcj3MAl2wpiif2jcI6yowRH&q={city}") #Dit haalt de locatie key op van de gegeven stad met de api.
    try: #Dit moet omdat als je bijvoorbeeld een land geeft of iets doms dan geeft ie een error
        locationKey = locationKey.json()[0]["Key"] # Het geeft een hele mik van info over de stad maar we hebben alleen de key nodig
    except:
        print("Stad niet gevonden of ongeldige invoer")
        time.sleep(1)
        HetWeer(username)
    response = requests.get(f'http://dataservice.accuweather.com/forecasts/v1/daily/1day/{locationKey}?apikey=NCkXL1pFDKcj3MAl2wpiif2jcI6yowRH&language=nl-nl&details=true&metric=true') #Dit haalt alle weersdata van de stad op van deze dag met de locatie key
    
    data = response.json() #Je krijgt een moker grote json structuur met alle data van het weer vandaag en met de onderstaande code halen we de data eruit die we willen hebben.
    #De eerder genoemde data ophalers
    voorspelling = data["DailyForecasts"][0]
    temperatuur = voorspelling["Temperature"]
    minTemp = temperatuur["Minimum"]["Value"]
    maxTemp = temperatuur["Maximum"]["Value"]
    GevoelsTemp = voorspelling["RealFeelTemperature"]["Maximum"]["Value"]
    weer = voorspelling["Day"]["IconPhrase"]
    luchtKwaliteit = voorspelling["AirAndPollen"][0]["Category"]
    onweerKans = voorspelling["Day"]["ThunderstormProbability"]
    regenKans = voorspelling["Day"]["RainProbability"]
    sneeuwKans = voorspelling["Day"]["SnowProbability"]
    ijsKans = voorspelling["Day"]["IceProbability"]
    wind = voorspelling["Day"]["Wind"]["Speed"]["Value"]
    windRichting = voorspelling["Day"]["Wind"]["Direction"]["Localized"]
    wolkenCover = voorspelling["Day"]["CloudCover"]
    wolkSoort = voorspelling["Day"]["LongPhrase"]
    source = voorspelling["Sources"]
    
    # En voorzelfsprekend printen we de data
    clear()
    print("Temperatuur:")
    print(f"De minimale temperatuur is vandaag {minTemp} graden")
    print(f"De maximale temperatuur is vandaag {maxTemp} graden")
    print(f"De temperatuur voelt vandaag aan als {GevoelsTemp} graden")
    print("\n\nWeer:")
    print(f"het weer is vandaag {weer}")
    print(f"De luchtkwaliteit is vandaag {luchtKwaliteit}")
    print(f"De kans op onweer is vandaag {onweerKans}%")
    print(f"De kans op regen is vandaag {regenKans}%")
    print(f"De kans op sneeuw is vandaag {sneeuwKans}%")
    print(f"De kans op ijs is vandaag {ijsKans}%")
    print(f"De windsnelheid is vandaag {wind} km/h")
    print(f"De windrichting is vandaag {windRichting}")
    print(f"De bewolking is vandaag {wolkenCover}%")
    print(f"De soort bewolking is vandaag: {wolkSoort}")
    print(f"\nBron: {source}")

    terug = (input("Druk op enter om verder te gaan\n"))
    if terug == "":
        AppPagina(username)

def main():
    username = AccountPagina()
    AppPagina(username)

main()