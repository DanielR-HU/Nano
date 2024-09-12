import random # Importeert de random module

LineBreak = "\n"*10


def WoordGuess():
    aantal_guesses = 0
    nummer = random.randint(1, 10) # Maakt het random nummer
    print(LineBreak,"\nJe hebt 3 kansen om het nummer te raden\n")

    while aantal_guesses < 3: # Dit zorgt er voor dat je maar 3 kansen hebt
        guess = input("Welk nummer tussen 1 en 10 denk je dat het is? \n")
        try: # Dit zorgt er voor dat als je geen nummer invoert, dat je het opnieuw kan proberen.
            guess = int(guess) # Dit probeert de input om te zetten naar een integer
            if 1 <= guess <= 10: # Dit zorgt er voor dat het nummer tussen 1 en 10 is
                aantal_guesses += 1 # Dit telt de aantal guesses op
                if guess == nummer: # Dit zorgt er voor dat als je het nummer goed hebt geraden, dat het programma stopt
                    print("\nGoed geraden!")
                    print("Je hebt het in", aantal_guesses, "keer geraden\n")
                    break
                elif guess < nummer: # Dit zorgt er voor dat als je het nummer fout hebt geraden, dat het programma zegt of het nummer hoger of lager is
                    print("\nTe laag\n")
                else:
                    print("\nTe hoog\n")
            else:
                print("\nDit nummer is niet tussen 1 en 10")
        except ValueError:
            print("\nDit is geen nummer\n")

    if aantal_guesses == 3 and guess != nummer: # Dit zorgt er voor dat als je 3 keer fout hebt geraden, dat het programma stopt en zegt wat het nummer was
        print("\nJe hebt het nummer niet geraden")
        print("Het nummer was", nummer)
WoordGuess()

# Van Daniel R
