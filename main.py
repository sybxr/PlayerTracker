import time
import requests
import os
#dont skid thx - syber (ilysm)
def banner():
    print("▄▄▄█████▓ ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀▓█████  ██▀███  ")
    print("▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒")
    print("▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒")
    print("░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  ")
    print("  ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒")
    print("  ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░")
    print("    ░      ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░")
    print(" ░        ░░   ░   ░   ▒   ░        ░ ░░ ░    ░     ░░   ░ ")
    print("           ░           ░  ░░ ░      ░  ░      ░  ░   ░     ")
    print("                            ░                               ")
    print("                        by syber")
    print("------------------------------------------------------------")


def getPlayersFromFile():
    try:
        with open("players.txt", 'r') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]
        return lines
    except FileNotFoundError:
        print("File 'players.txt' not found.")
        return []


def checkApiFile():
    try:
        with open("apikey.txt", 'r') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]
        return lines
    except FileNotFoundError:
        print("File 'apikey.txt' not found.")
        return []


def startup():
    print("starting up")


def choice():
    while True:
        inp = input("start, exit, setup, or help?")
        if inp == "start":
            return
        elif inp == "exit":
            exit()
        elif inp == "setup":
            print("---------------------------------------------------------------------------------")
            print("put in the same directory 2 .txt files, players.txt and apikey.txt")
            print("in players.txt, add player igns, 1 per line. ")
            print("in apikey.txt, put your hypixel developer api key, obtained from developer.hypixel.net")
            print("make sure to have requests installed - pip install requests")
            print("---------------------------------------------------------------------------------")
        elif inp == "help":
            print("---------------------------------------------------------------------------------")
            print("dm me on disc: sybxr")
            print("---------------------------------------------------------------------------------")


def startTracker(trackedPlayers=[]):
    playerUUIDS = []
    try:
        with open("apikey.txt", 'r') as file:
            content = file.read()
            print("your apikey is " + content)
    except FileNotFoundError:
        print("File 'apikey' not found.")
        return ()

    for playerName in trackedPlayers:
        response = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{playerName}')
        if response.status_code == 200:
            playerUUIDS.append(response.json()["id"])
        else:
            print(f'can not find {playerName} uuid')
    time.sleep(5)

    
    while True:
        os.system("cls")
        banner()
        for uuid in playerUUIDS:
            response = requests.get(f'https://api.hypixel.net/status?key={content}&uuid={uuid}')
            if response.status_code == 200:
                data = response.json()
                if data and data.get('session') and data['session'].get('mode') == 'PIT':
                    response2 = requests.get(f'https://sessionserver.mojang.com/session/minecraft/profile/{uuid}')
                    user = (response2.json()["name"])
                    print(user + " IS ON PIT! ---   " + time.ctime())
            else:
                print("FAILED TO CONTACT HYPIXEL API")
        print("---------------------------------------")
        time.sleep(20)


banner()
startup()
print()
players = getPlayersFromFile()
checkApiFile()
print("Players added:")
print(players)
print()
choice()
print("STARTING!")
startTracker(players)