#nano 2.0

import time
import random
import os

#main functies

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def inloggen():
    clear()
    print("Welkom bij Nano")
    print("Log in om verder te gaan")
    print("Gebruikersnaam:")
    username = input()
    print("Wachtwoord:")
    password = input()
    with open("users.txt", "r") as file:
        for line in file:
            user, pw = line.strip().split(",")
            if user == username and pw == password:
                print(f"Welkom {username}")
                time.sleep(1)
                username = username
                password = password
                return username and password
            else:
                print("Gebruikersnaam of wachtwoord is fout")
                time.sleep(1)
                return AccountPagina()
        print("Gebruikersnaam of wachtwoord is fout")
def registreren():
    clear()
    print("Welkom bij Nano")
    print("Registreer uw account")
    print("Gebruikersnaam:")
    username = input()
    print("Wachtwoord:")
    password = input()
    with open("users.txt", "a") as file:
        file.write(username + "," + password + "\n")
    print("Account gemaakt")
    time.sleep(1)
    return AccountPagina()

def AccountPagina():
    clear()
    print("Inlog pagina")
    keuze = input("1. Inloggen\n2. Registreren\n")
    if keuze == "1":
        inloggen()
    elif keuze == "2":
        registreren()
    else:
        print("Foute invoer")
        time.sleep(1)
        AccountPagina()

def AppPagina(username):
    clear()
    print("Welkom bij Nano")
    print("Kies een app")
    print("1. CijferGuess\n2. Exit")
    keuze = input()
    if keuze == "1":
        Games.CijferGuess(username)
    elif keuze == "2":
        exit()
    else:
        print("Foute invoer")
        time.sleep(1)
        AppPagina()

class Games:
    def CijferGuess(username):
        print(f"Welkom {username}")


def main(username):
    AccountPagina()
    AppPagina(username)


main(username)