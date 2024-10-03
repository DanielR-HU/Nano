import tkinter as tk

def window():
    window = tk.Tk()
    window.title("Hello World")
    window.geometry('350x200')
    lbl = tk.Label(window, text="Hello")
    lbl.grid(column=0, row=0)
    window.mainloop()

def CijferGuess(username):
    highscore = 0
    with open("HighscoreCijfer.txt", "r") as file:
        for line in file:
            user, highscoreL = line.strip().split(",")
            if user == username:
                highscore = highscoreL
                break
    clear()
    Cijfer_Graad = input(f"\t\t\tWelkom bij het cijfer guess spel {username}!\n\t\t\t\tJe highscore is {highscore}\n\t\tVul het cijfer in van de moeilijkeids graad die je wilt. \n\n\nWil je het makkelijk, normaal of moeilijk maken?\n 8 = makkelijk\n 4 = normaal\n 3 = moeilijk\n 1 = onmogelijk\n\n")
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
        guess = input("Welk nummer tussen 1 en 10 denk je dat het is? \n")
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
                        main()
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
            main()


def main():
    window()

main()  