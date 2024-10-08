""" 
Dit is de NanoXL opdracht van Daniel Roodenburg.
Geprogameerd in Visual Studio Code met Github copilot.
Github copilot is alleen gebruikt om het typen van de code te versnellen.
De code heb ik voor het meeste zelf bedacht en geschreven.
Natuurlijk heb ik stukjes code online opgezocht op random forums enzo.

"""




import time
import random
import os
import datetime
try:
    import requests
except:
    os.system("pip install requests")
    import requests
try:
    import tkinter as tk
except:
    os.system("pip install tkinter")
    import tkinter as tk
import json

#main functies
def Files():
    if not os.path.exists("users.json"):
        with open("users.json", "w") as file:
            json.dump({}, file)
    if not os.path.exists("HighscoresNummer.json"):
        with open("HighscoresNummer.json", "w") as file:
            json.dump({}, file)

    if not os.path.exists("LogGalgje.txt"):
        with open("LogGalgje.txt", "w") as file:
            file.write("")
    
    if not os.path.exists("WoordenlijstMakkelijk.txt"):
        with open("WoordenlijstMakkelijk.txt", "w") as file:
            file.write("hond\nkat\nboom\nbal\nauto\nhuis\nmuis\nstoel\nboek\nfiets\n")
    
    if not os.path.exists("WoordenlijstNormaal.txt"):
        with open("WoordenlijstNormaal.txt", "w") as file:
            file.write("tafel\nappel\nschool\nwater\nkasteel\nvriend\ntrolley\nlaptop\nleraar\nmuziek\n")
    
    if not os.path.exists("WoordenlijstMoeilijk.txt"):
        with open("WoordenlijstMoeilijk.txt", "w") as file:
            file.write("paradox\nsubstantieel\nonverzettelijk\nepistemologie\nambivalentie\nstereotypisch\nnostalgisch\ntranscendent\nhypothese\nijdelheid\n")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear') # Dit zorgt er voor dat de cmd op windows en linux devices wordt gecleared

def inloggen():
    clear()
    print("Welkom bij Nano\n")
    print("Log in om verder te gaan")
    print("Gebruikersnaam:")
    username = input("> ")
    print("\nWachtwoord:")
    password = input("> ")

    data = json.load(open("users.json"))
    if username in data:
        if data[username] == password:
            clear()
            print(f"Welkom {username}")
            time.sleep(1)
            return username
        else:
            print("Wachtwoord is fout")
            time.sleep(1)
            return AccountPagina()
    else:
        print("Gebruikersnaam is fout of bestaat niet")
        time.sleep(1)
        return AccountPagina()
    
def registreren():
    clear()
    print("Welkom bij Nano\n")
    print("Registreer uw account")
    print("Gebruikersnaam:")
    username = input(">")
    print("\nWachtwoord:")
    password = input(">")

    with open("users.json", "r") as file:
        data = json.load(file)

    if username in data:
        print("Gebruikersnaam bestaat al")
        time.sleep(1)
        AccountPagina()
    else:
        data[username] = password
        with open("users.json", "w") as file:
            json.dump(data, file, indent=4) # Dit zorgt er voor dat de data in de json file wordt gezet en indent=4 zorgt er voor dat het netjes wordt opgeslagen
        print("Registratie succesvol")

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
    elif keuze == "admin": # Admin bypass
        return "admin"
    else:
        print("Foute invoer")
        time.sleep(1)
        AccountPagina()

def AppPagina(username):
    clear()
    print("Welkom bij Nano\n")
    print("Kies een app:")
    print("1. CijferGuess\n2. Galgje\n3. Galgje log\n4. Boter kaas en eieren (GUI)\n5. Het weer\n6. EONET (NASA)\n7. Recepten\n8. Exit\n")
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
        EONET(username)
    elif keuze == "7":
        Recepten(username)
    elif keuze == "8":
        exit()
    else:
        print("Foute invoer")
        time.sleep(1)
        AppPagina(username)

def CijferGuess(username):
    highscore = 0
    with open("HighscoresNummer.json", "r") as file:
        data = json.load(file)

    if username in data:
        highscore = data[username]

    else:
        data[username] = highscore
        with open("HighscoresNummer.json", "w") as file:
            json.dump(data, file, indent=4)
        
    clear()
    Cijfer_Graad = input(f"\t\t\tWelkom bij het cijfer guess spel {username}!\n\t\t\t   --------Je highscore is {highscore}--------\n\n\t\tVul het cijfer in van de moeilijkeids graad die je wilt. \n\n\nWil je het makkelijk, normaal of moeilijk maken?\n 8 = makkelijk\n 4 = normaal\n 3 = moeilijk\n 1 = onmogelijk\n\n> ")
    if Cijfer_Graad.isdigit():
        Cijfer_Graad = int(Cijfer_Graad)
        if Cijfer_Graad == 1 or Cijfer_Graad == 3 or Cijfer_Graad == 4 or Cijfer_Graad == 8:
            clear()
        else:
            print("Dit is geen geldige keuze")
            time.sleep(1)
            CijferGuess(username)
    else:
        print("\nDit is geen nummer")
        time.sleep(1)
        CijferGuess(username)

    aantal_guesses = 0
    aantal_guesses = int(aantal_guesses)
    nummer = random.randint(1, 10)

    while aantal_guesses < Cijfer_Graad:
        print(f"\n\nJe hebt gekozen voor {Cijfer_Graad} kansen om te raden\n")
        print(f"Je hebt {aantal_guesses} keer geraden\n")
        guess = input("Welk nummer tussen 1 en 10 denk je dat het is? \n\n> ")
        if guess.isnumeric():
            guess = int(guess)
            if 1 <= guess <= 10:
                aantal_guesses += 1
                if guess == nummer:
                    clear()
                    print("\nGoed geraden!")
                    print(f"Je hebt het in {aantal_guesses} keer geraden\n")
                    if int(aantal_guesses) < int(highscore) or int(highscore) == 0:
                        print("Je hebt een nieuwe highscore!")
                        highscore = aantal_guesses
                        data[username] = highscore
                        with open("HighscoresNummer.json", "w") as file:
                            json.dump(data, file, indent=4)
                    terug = (input("Druk op enter om verder te gaan\n"))
                    if terug == "":
                        AppPagina(username)
                elif guess < nummer: 
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

    if aantal_guesses == Cijfer_Graad and guess != nummer:
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
        
        
        Geraden = False
        Woord = Woordenlijst[random.randrange(0, len(Woordenlijst))]
        Letters = list(str.lower(Woord))
        GeradenLetters = ['_' for _ in Letters] # Dit maakt een lijst met dehoeveelheid letters als streepjes.
        Fouten = 0
        
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
        print(str(GeradenLetters).replace("'", "").replace("[","").replace("]","").replace(",","")) # Dit heb ik gedaan omdat het werkte, de code ziet er niet mooi uit maar boeie.
        while Geraden == False:
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
                    Geraden = True
                    #GERADEN!!!!
                    datum = datetime.datetime.now()
                    with open("LogGalgje.txt", "a") as file: # Logging voor de log file
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
                    terug = (input("\nDruk op enter om verder te gaan\n"))
                    if terug == "":
                        AppPagina(username)

                print("\nJe hebt de letter fout\n")
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
    root = tk.Tk()
    root.title("Boter, Kaas en Eieren")

    speler = "X"
    bord = [["" for _ in range(3)] for _ in range(3)]
    def switch_player(): 
        nonlocal speler # Dit zorgt er voor dat de speler variabele global is omdat het helaas niet anders kan
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

    # Variabele k is de variabele die de tekst van de button veranderd zie de rij van variabele k1_1 k1_2 etc.

    def button_click(button, k, rij, kolom):
        if bord[rij][kolom] == "":
            bord[rij][kolom] = speler
            k.set(speler) 
            if check_winnaar():
                clear()
                print(f"{speler} heeft gewonnen!")
                root.destroy()
            switch_player()

    k1_1 = tk.StringVar()
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
    
    root.mainloop()
    terug = (input("Druk op enter om verder te gaan\n"))
    if terug == "":
        AppPagina(username)

def HetWeer(username):
    clear()
    
    while True:
        city = input("Voer plaats in:\n> ")
        locationKey = requests.get(f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey=NCkXL1pFDKcj3MAl2wpiif2jcI6yowRH&q={city}") #Dit haalt de locatie key op van de gegeven stad met de api.
        try: #Dit moet omdat als je bijvoorbeeld een land geeft of iets doms dan geeft ie een error
            locationKey = locationKey.json()[0]["Key"] # Het geeft een hele mik van info over de stad maar we hebben alleen de key nodig
            break
        except:
            print("Stad niet gevonden of ongeldige invoer")
            time.sleep(1)
            clear()
            
        
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
    Dag = voorspelling["Day"]["LongPhrase"]
    source = voorspelling["Sources"]
    
    
    clear()
    print(f"Vandaag in {city}:\n")
    print("Temperatuur:")
    print(f"De minimale temperatuur is vandaag {minTemp} graden")
    print(f"De maximale temperatuur is vandaag {maxTemp} graden")
    print(f"De temperatuur voelt vandaag aan als {GevoelsTemp} graden")
    print("\n\nWeer:")
    print(f"het weer is vandaag: {weer}")
    print(f"De luchtkwaliteit is vandaag {luchtKwaliteit}")
    print(f"De kans op onweer is vandaag {onweerKans}%")
    print(f"De kans op regen is vandaag {regenKans}%")
    print(f"De kans op sneeuw is vandaag {sneeuwKans}%")
    print(f"De kans op ijs is vandaag {ijsKans}%")
    print(f"De windsnelheid is vandaag {wind} km/h")
    print(f"De windrichting is vandaag {windRichting}")
    print(f"De bewolking is vandaag {wolkenCover}%")
    print(f"Het weer is vandaag: {Dag}")
    print(f"\nBron: {source}")

    terug = (input("Druk op enter om verder te gaan\n"))
    if terug == "":
        AppPagina(username)

def EONET(username):
    clear()
    skip = False
    if skip == False:
        print("Welkom bij EONET!\nDit is een programma dat de data van NASA haalt over natuurrampen\nZometeen moet je een categorie kiezen en dan krijg je alle events van die categorie van de afgelopen 31 dagen.\nHet kan zijn dat er niks is.\n")
        input("Druk op enter om verder te gaan\n")
        clear()
    try:
        response = requests.get("https://eonet.gsfc.nasa.gov/api/v2.1/categories?days=31")
        response.raise_for_status() #Dit moest ofzo voor errors. Ik zag het online en het werkte denk ik als er een error is.
        categories = response.json()["categories"]
        
        # Dit maakt een dictionary van de categorieën, waarbij de titel de key is en de hele categorie de value
        category_map = {category["title"]: category for category in categories}
        
        # Dit print alle categorieën
        for title, category in category_map.items():
            print(f"{title}:\n   {category['description']}")

        keuze = input("\nSchrijf de categorie precies over a.u.b.\nKies een categorie:\n> ")
        if keuze in category_map:
            categorieID = category_map[keuze]['id'] # Dit haalt de categorieID op van de gekozen categorie
            responseCat = requests.get(f"https://eonet.gsfc.nasa.gov/api/v2.1/categories/{categorieID}?days=31") # Dit haalt de data op van de gekozen categorie.
            event_map = {event["title"]: event for event in responseCat.json()["events"]} # Dit maakt een dictionary van de events, waarbij de titel de key is en de hele event de value
            if not event_map:
                clear()
                print("Er zijn geen events in deze categorie")
            else:
                clear()
                for title, event in event_map.items():
                    print(f"{title}:\n   {event['geometries'][0]['date']}")
                terug = (input("Druk op enter om terug te gaan\n"))
                if terug == "":
                    AppPagina(username)
        else:
            clear()
            print("Ongeldige categorie gekozen.")
        terug = (input("\nDruk op enter om terug te gaan\n"))
        if terug == "":
            EONET(username) 

    #Dit heb ik gehaald van het internet en ik weet niet of het werkt omdat ik nog geen error heb gehad
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        terug = (input("\nDruk op enter om terug te gaan\n"))
        if terug == "":
            EONET(username)

def Recepten(username):
    def ReceptChooser():
        naam = input("\nWelk recept wilt u bekijken?\n> ")
        try:
            data = requests.get(f"https://www.themealdb.com/api/json/v1/1/search.php?s={naam}")
        except:
            print("Iets is fout gegaan")
            Recepten(username)
        if data.json()["meals"] == None:
            print("Recept niet gevonden")
            terug = (input("\nDruk op enter om verder te gaan\n"))
            if terug == "":
                AppPagina(username)
        strMeal = data.json()["meals"][0]["strMeal"]
        strArea = data.json()["meals"][0]["strArea"]
        strInstructions = data.json()["meals"][0]["strInstructions"]
        clear()
        print(f"Naam: {strMeal}\nPlaats: {strArea}\nInstructies: {strInstructions}\n\n\nIngrediënten:")
        for i in range(1, 21):
            ingredient = data.json()["meals"][0][f"strIngredient{i}"]
            if ingredient != "":
                print(f"{ingredient} - {data.json()["meals"][0][f"strMeasure{i}"]}")
            else:
                break
        terug = (input("\nDruk op enter om verder te gaan\n"))
        if terug == "":
            AppPagina(username)

    def CheckNone():
        if data.json()["meals"] == None:
            print("Recept niet gevonden")
            terug = (input("\nDruk op enter om verder te gaan\n"))
            if terug == "":
                AppPagina(username)

    clear()
    print("Welkom bij de recepten app.\n")
    keuze = input("Wilt u zoeken op naam, categorie, ingredient, plaats of random?\n> ").lower()
    if keuze == "naam":
        naam = input("Voer de naam van het recept in:\n> ")
        try:
            data = requests.get(f"https://www.themealdb.com/api/json/v1/1/search.php?s={naam}")
        except:
            print("Iets is fout gegaan")
            Recepten(username)
        CheckNone()
        strMeal = data.json()["meals"][0]["strMeal"]
        strArea = data.json()["meals"][0]["strArea"]
        strInstructions = data.json()["meals"][0]["strInstructions"]
        clear()
        print(f"Naam: {strMeal}\nPlaats: {strArea}\nInstructies: {strInstructions}\n\n\nIngrediënten:")
        for i in range(1, 21):
            ingredient = data.json()["meals"][0][f"strIngredient{i}"]
            if ingredient != "":
                print(ingredient + " - " + data.json()["meals"][0][f"strMeasure{i}"])
            else:
                break
        terug = (input("\nDruk op enter om verder te gaan\n"))
        if terug == "":
            AppPagina(username)

    elif keuze == "categorie":
        categories = requests.get("https://www.themealdb.com/api/json/v1/1/categories.php")
        categories = categories.json()["categories"]
        clear()
        for category in categories:
            print(category["strCategory"])
        
        categorie = input("\nVoer de categorie van het recept in:\n> ")
        data = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?c={categorie}")
        CheckNone()
        clear()
        for meal in data.json()["meals"]:
            print(meal["strMeal"])
        ReceptChooser()

    elif keuze == "ingredient":
        clear()
        ingredient = input("Voer het ingredient van het recept in:\n> ")
        data = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}")
        CheckNone()
        clear()
        for meal in data.json()["meals"]:
            print(meal["strMeal"])
        ReceptChooser()

    elif keuze == "plaats":
        plaatsen = requests.get("https://www.themealdb.com/api/json/v1/1/list.php?a=list")
        for plaats in plaatsen.json()["meals"]:
            print(plaats["strArea"])
        plaats = input("Voer de plaats van het recept in:\n> ")
        data = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?a={plaats}")
        CheckNone()
        clear()
        for meal in data.json()["meals"]:
            print(meal["strMeal"])
        ReceptChooser()

    elif keuze == "random":
        data = requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
        strMeal = data.json()["meals"][0]["strMeal"]
        strArea = data.json()["meals"][0]["strArea"]
        strInstructions = data.json()["meals"][0]["strInstructions"]
        clear()
        print(f"Naam: {strMeal}\nPlaats: {strArea}\nInstructies: {strInstructions}\n\n\nIngrediënten:")
        for i in range(1, 21):
            ingredient = data.json()["meals"][0][f"strIngredient{i}"]
            if ingredient != "":
                print(ingredient + " - " + data.json()["meals"][0][f"strMeasure{i}"])
            else:
                break
        terug = (input("\nDruk op enter om verder te gaan\n"))
        if terug == "":
            AppPagina(username)



def main():
    Files()
    username = AccountPagina()
    AppPagina(username)
    
main()