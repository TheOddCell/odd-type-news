# The News Client

import urllib.request    # For requests
import sys               # For closing the program
import os                # For clearing the screen, for getting the terminal size.
from pathlib import Path # For getting the last saved server

oddclientinfo = Path("./oddclientinfo.txt")
defaultserver = "https://otn.oddcell.ca/helpnews/"

def get_server():
    if oddclientinfo.is_file():
        with open(oddclientinfo, "r") as f:
            return f.read().strip()
    else:
        with open(oddclientinfo, "w") as f:
            f.write(defaultserver)
        return defaultserver
        

server = get_server()



def allOSclear(): # All OS's
    os.system("clear") # For *nix Systems (unix based systems)
    if os.name == 'nt': # If windows, will clear error message. if unix like, no errors.
        os.system("cls")   # For Windows Systems (NT systems)

def dash():
    dashs = ""
    while not len(dashs) == os.get_terminal_size().columns:
        dashs = f"{dashs}-"
    return dashs

def request(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    contents = urllib.request.urlopen(req).read().decode('utf-8').strip()
    return contents

def articleinput():
    global server
    articles = int(request(f"{server}num.txt"))
    userinput = input("Choose a post, type \"exit\" to exit, or type \"switch\" to switch servers.\n> ")
    if userinput == "exit":
        sys.exit(0)
    elif userinput == "switch":
        server = input(f"Current server: {server}\nDefault Server:{defaultserver}\nPlease choose a server URL: ")
        with open(oddclientinfo, "w") as f:
            f.write(server)
        return articleinput()
        
    try:
        intput = int(userinput)
    except:
        print("Error: not integer.")
        return articleinput()
    if intput < 1:
        print("Error: Less than 0.")
        return articleinput()
    elif intput > articles + 1:
        print("Error: Article does not exist.")
        return articleinput()
    else:
        return intput

def main():
    allOSclear()
    articles = int(request(f"{server}num.txt"))
    disc = request(f"{server}disc.txt").replace("\n", "").replace("\\", "\n")
    title = request(f"{server}title.txt")
    print(f"Hello!\nWelcome to the OddTypeNews client terminal.")
    while True:
        print(f"You are connected to {server}.\n\nTitle: {title}\nDiscription:\n{disc}\n")
        articles = int(request(f"{server}num.txt"))
        print(f"There are {articles + 1} posts available.")
        usrinput = articleinput()
        allOSclear()
        metadata = request(f"{server}news/{usrinput - 1}/metadata.txt").replace("\n", "").replace("\\", "\n")
        content = request(f"{server}news/{usrinput - 1}/content.txt").replace("\n", "").replace("\\", "\n")
        print(f"Article {usrinput}\n{metadata}\n{dash()}\n\n{content}\n{dash()}\n\nPress enter to view another article or exit.")
        input()
        allOSclear()
main()